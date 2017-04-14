n = int(input())
grid = [[j for j in input().strip()] for i in range(n)]

a,b,c,d = input().split()

def ways(j,k):
    adnodes = set()
    if j+1<n and k+1<m and grid[j+1][k+1] == '.':
        adnodes.add((j+1,k+1))
    if j+1<n and k<m and grid[j+1][k] == '.':
        adnodes.add((j+1,k))
    if j<n and k+1<m and grid[j][k+1] == '.':
        adnodes.add((j,k+1))
    if j-1>=0 and k-1>=0 and grid[j-1][k-1] == '.':
        adnodes.add((j-1,k-1))
    if j>=0 and k-1>=0 and grid[j][k-1] == '.':
        adnodes.add((j,k-1))
    if j-1>=0 and k>=0 and grid[j-1][k] == '.':
        adnodes.add((j-1,k))
    if j+1<n and k-1>=0 and grid[j+1][k-1] == '.':
        adnodes.add((j+1,k-1))
    if j-1>=0 and k+1<m and grid[j-1][k+1] == '.':
        adnodes.add((j-1,k+1))
    return adnodes

visited = set()

for j in range(n):
    for k in range(n):
        if (j,k) not in visited and grid[j][k]!='X' and (j,k)!=():

