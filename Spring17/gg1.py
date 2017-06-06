n= 10
def b0():
    return
def b1(n):
    return n
def b2(n):
    sum = 0
    for i in range(n):
        sum+=b1(n-i-1)
        print(sum)
    return sum
def b3(n):
    sum = 0
    for i in range(n):
        sum+=b2(n-i-1)
    return sum
def b4(n):
    sum = 0
    for i in range(n):
        sum+=b3(n-i-1)
    return sum
def b5(n):
    sum = 0
    for i in range(n):
        sum+=b4(n-i-1)
    return sum
def b7(n):
    sum = 0
    for i in range(n):
        sum+=b6(n-i-1)
    return sum
def b6(n):
    sum = 0
    for i in range(n):
        sum+=b5(n-i-1)
    return sum
def b8(n):
    sum = 0
    for i in range(n):
        sum+=b7(n-i-1)
    return sum
def b9(n):
    sum = 0
    for i in range(n):
        sum+=b8(n-i-1)
    return sum

def main ():
    l = []
    d = [b1,b2,b3,b4,b5,b6,b7,b8,b9]
    # for j in range(10):
    #     k = []
    #     for i in range(len(d)):
    #         d[i](i+1)
    print(b3(3))

main()