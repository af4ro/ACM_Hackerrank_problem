def number_needed(a, b):
    count = 0
    i = 0
    while i<len(a):
        temp = b.find(a[i])
        if (temp==-1):
            # b = b[0:temp]+b[temp+1:]
            if i!=len(a)-1:
                a = a[0:i] + a[i+1:]
            else:
                a = a[0:i]
            count+=1
            continue
        i+=1
    j=0
    while j <len(b):
        temp = a.find(b[j])
        if (temp == -1):
            # a = a[0:temp] + a[temp + 1:]
            if j != len(b) - 1:
                b = b[0:j] + b[j + 1:]
            else:
                b= b[0:j]
            count += 1
            continue
        j+=1
    return count


a = input().strip()
b = input().strip()

print(number_needed(a, b))
