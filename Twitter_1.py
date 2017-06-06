final_list = []
num_con = ['01','02','03','04','05','06','07','08','09']
date_dict = {'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04', 'May': '05', "Jun": '06', 'Jul': '07', 'Aug': '08', 'Sep': '09', 'Oct': '10', 'Nov' : '11', 'Dec':'12'}

try:
    while True:
        cursor = 0

        final_list.append({"endpoint":"", 'hit': 0, 'count':1, 'year':0, 'month':0, 'day':0,'hour':0, 'minute':0 , 'final':"", "srate":0.00})
        temp = input()
        temp_date = (temp[temp.find("[")+1:temp.find(":")]).split("/")
        final_list[-1]["year"] = int(temp_date[2])
        final_list[-1]["month"] = int(date_dict[temp_date[1]])
        final_list[-1]["day"] = int(temp_date[0])
        final_list[-1]["final"]= "{}-{}-{}".format(temp_date[2],date_dict[temp_date[1]],temp_date[0])
        cursor = temp.find(":")
        final_list[-1]['hour'] = int(temp[cursor+1:cursor+3])
        final_list[-1]['minute'] = int(temp[cursor+4:cursor+6])
        if temp[cursor+10] == "+":
            t = temp[temp.find("+")+1:temp.find("+")+5]
            final_list[-1]['hour'] += int(t[0:3])
            final_list[-1]['minute'] += int(t[2:])
        else:
            final_list[-1]['hour'] += int(temp[cursor+11:cursor+13])
            final_list[-1]['minute'] += int(temp[cursor+12:cursor+14])

        cursor = temp.find("\"")
        cursor += temp[cursor:].find('/')
        if temp.find("?") == -1:
            s = cursor + temp[cursor:].find(' ')
            final_list[-1]["endpoint"] = temp[cursor:s]
        else:
            final_list[-1]["endpoint"] = temp[cursor:temp.find("?")]

        cursor+= temp[cursor:].find("\"")+2
        if int(temp[cursor]) != 5:
            final_list[-1]['hit'] += 1

        if len(final_list)>1:
            if final_list[-2]['endpoint'] == final_list[-1]['endpoint']:
                if (final_list[-2]['year'] == final_list[-1]['year']) & (final_list[-2]['month'] == final_list[-1]['month']) & (final_list[-2]['day'] == final_list[-1]['day']) & (final_list[-2]['hour'] == final_list[-1]['hour']) & (final_list[-2]['minute'] == final_list[-1]['minute']):
                    final_list[-2]['hit']+= final_list [-1]['hit']
                    final_list[-2]['count']+= final_list [-1]['count']
                    final_list.pop()
except EOFError:
    if final_list[-1]["endpoint"] == "":
        final_list.pop()
    for dic in range(len(final_list)):
        final_list[dic]['srate'] = (float(final_list[dic]['hit'])/float(final_list[dic]['count']))*100
    final_list.sort(key= lambda x: (x['hour'],x['minute'],x['endpoint']))
    for i in final_list:
        print("{}T{}:{} {} {:.2f}".format(i["final"],(i['hour'] if i['hour'] > 9 else num_con[i['hour']-1]),(i['minute'] if i['minute'] > 9 else num_con[i['minute']-1]),i['endpoint'],i['srate']))