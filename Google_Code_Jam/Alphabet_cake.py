n= int(input())
cake= []
def fill_s(grid,a,b):
    for j in range(a):
        for k in range(b):
            temp = grid[j][k]
            flag = 0
            while k<b:
                if grid[j][k] == '?':
                    grid[j][k] = temp
                    flag = 1
                    k += 1
                else:
                    break

            if flag:
                break
            flag = 0
            while j<a:
                if grid[j][k] == '?':
                    grid[j][k] = temp
                    flag = 1
                    j += 1
                else:
                    break
            if flag:
                continue
            flag = 0
            while k>=0:
                if grid[j][k] == '?':
                    grid[j][k] = temp
                    flag = 1
                    k -= 1
                else:
                    break
            if flag:
                continue
            flag = 0
            while j>=0:
                if grid[j][k] == '?':
                    grid[j][k] = temp
                    j -= 1
                else:
                    break
    return grid

for i in range(n):
    a = input().split()
    temp = [input().split() for j in range(int(a[0]))]
    print(fill_s(temp,int(a[0]),int(a[1])))

