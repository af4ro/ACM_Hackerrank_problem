lims = input().strip().split(',')
start = {"str_rep":lims[0].strip(), 'year':int((lims[0].strip())[0:4]),'month':int((lims[0].strip())[5:])}
end = {"str_rep":lims[1].strip(), 'year':int((lims[1].strip())[0:4]),'month':int((lims[1].strip())[5:])}
input()
activity = {}
try:
    while True:
        temp = input().strip()
        a = temp[:temp.find(',')].strip().split('-')
        year = int(a[0])
        month = int(a[1])
        if (start['year']==year) and (start['month']>month):
            continue
        elif (year==end['year']) and (month>=end['month']):
            continue
        elif (year < start['year']) or (year > end['year']):
            continue
        else:
            date = temp[:temp.find(',')-3].strip()
            act = temp[temp.find(',')+1:temp.rfind(',')].strip()
            count = int(temp[temp.rfind(',')+1:].strip())
            if date in activity.keys():
                if act in activity[date].keys():
                    activity[date][act] += count
                else:
                    activity[date][act] = count
            else:
                activity[date] = {'date':(year,month)}
                activity[date][act] = count

except EOFError:
    for dates in sorted(activity.keys(),key= lambda x: (activity[x]['date'][0],activity[x]['date'][1]),reverse = True):
        print(dates + "".join([", {}, {}".format(i,activity[dates][i]) for i in sorted(activity[dates].keys()) if i!='date']))