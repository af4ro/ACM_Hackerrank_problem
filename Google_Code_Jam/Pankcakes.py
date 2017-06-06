def pank(panks, num):
    if (panks == ("+"*len(panks))):
        return 0
    


n = input()
for i in range(int(n)):
    s,m = input().split()
    print("Case #{}: {}".format(i+1,pank(s,int(m))))





