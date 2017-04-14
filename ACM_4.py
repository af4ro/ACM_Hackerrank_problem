
def recursive_check(n,m,grid, i, j, con):
    if (j+1)<=m:
        if grid[i][j+1]==1:


    return con

largest_region = [0]
visited = []

def getBiggestRegion(grid):
    n = int(input().strip())
    m = int(input().strip())
    grid = []
    for grid_i in range(n):
        grid_t = list(map(int, input().strip().split(' ')))
        grid.append(grid_t)
    print(grid)
    for i in grid:
        for j in i:
            if (j==1) and ((i,j) not in visited):
                largest_region.append(recursive_check(n,m,grid,i,j,largest_region[-1]))
    return max(largest_region)


getBiggestRegion([])