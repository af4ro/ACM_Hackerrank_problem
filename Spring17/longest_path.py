n = int(input())
colors = input().strip().split()
m = input()
result = []
count = 0
for i in colors:
    if int(i) == 0:
        result.append(count)
        count = 0
    count+=1
print(max(result))