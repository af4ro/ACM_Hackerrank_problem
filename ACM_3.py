def pairs(a,k):
    # a is the list of numbers and k is the difference value
    a.sort()
    c = set(a)
    b = a[-1]
    answer = 0
    for i in a:
        if i >= b:
            break
        elif (i+k) in c:
            answer+=1
    return answer

print(pairs([10,8,6,4,2],2))