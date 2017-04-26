n, m = input().split()
terms = [int(i) for i in input().split()]
if int(n) <= 1:
    print(-1)
else:
    count = 0
    while terms[0]<int(m) and len(terms)>1:
        temp = terms[0] + (terms[1]*2)
        terms = terms[2:]
        terms.append(temp)
        terms.sort()
        count +=1
    print(count)