n = int(input())

# def do_it(N,P,needed, ing):
#     results= []
#     counter = 0
#     for i in ing:
#         count = 0
#         for j in i:
#             temp1 = int(int(j)/int(needed[counter]))
#             if  abs(int(j)-(temp1*int(needed[counter]))) > abs(int(j)-((temp1+1)*int(needed[counter]))):
#                 temp1 +=1
#             if int(j)<= (1.1*temp1*int(needed[counter])) and int(j)>= (0.9*temp1*int(needed[counter])):
#                 count+=1
#         results.append(count)
#         counter+=1
#     print(min(results))

def do_it(N,P,needed, ing):
    counter = 0
    temps = []
    keys = []
    for j in ing[0]:
        temp1 = int(int(j) / int(needed[counter]))
        if abs(int(j) - (temp1 * int(needed[counter]))) > abs(int(j) - ((temp1 + 1) * int(needed[counter]))):
            temp1 += 1
        if int(j) <= (1.1 * temp1 * int(needed[counter])) and int(j) >= (0.9 * temp1 * int(needed[counter])):
            temps.append(temp1)
            keys.append(1)
        else:
            temps.append(-1)
            keys.append(0)
        counter+=1

    print(temps,keys)
    for i in range(1,N):
        for j in range(P):
            if keys[j]!= 0 and int(ingrediants[i][j]) <= (1.1 * temps[j] * int(needed[j])) and int(j) >= (0.9 * temps[j] * int(needed[j])):
                pass
            else:
                keys[j] = 0
    print(sum(keys))

for i in range(n):
    N,P = input().split()
    needed = input().split()
    ingrediants= []
    for j in range(int(N)):
        ingrediants.append(input().split())
    do_it(int(N),int(P),needed,ingrediants)
    # print(ingrediants)