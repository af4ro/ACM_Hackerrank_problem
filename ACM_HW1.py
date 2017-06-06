
import sys


n = int(input().strip())
A = [int(A_temp) for A_temp in input().strip().split(' ')]
min_dist =10000
for i in range(n):
    if A[i] in A[i+1:]:
        if (A[i+1:].index(A[i])+1) < min_dist:
            min_dist = A[i+1:].index(A[i])+1

if min_dist == 10000:
    print(-1)
else:
    print(min_dist)