from collections import defaultdict
def sums(t, not_to):
    s = 0
    k = [t]
    visited = []
    while k != []:
        if (k[0]!= not_to) and (k[0] not in visited):
            if child_dict[k[0]] != []:
                k.extend(child_dict[k[0]])
            s+=int(vals[int(k[0])-1])
            visited.append(k[0])
        k.pop(0)
    return s


child_dict = defaultdict(list)
n = int(input())
vals = input().strip().split()
total_sum  = sum([int(i) for i in vals])
bonds = []
node_sum = {}
def main():
    for i in range(n-1):
        bonds.append(tuple(input().split()))
        b = bonds[-1]
        child_dict[b[0]].append(b[1])
        if b[0] not in node_sum.keys():
            node_sum[b[0]] = int(vals[int(b[0])-1]) + int(vals[int(b[1])-1])
        else:
            node_sum[b[0]]+= int(vals[int(b[1])-1])
        child_dict[b[1]].append(b[0])
        if b[1] not in node_sum.keys():
            node_sum[b[1]] = int(vals[int(b[0])-1]) + int(vals[int(b[1])-1])
        else:
            node_sum[b[1]]+= int(vals[int(b[0])-1])


    min = total_sum
    for i,j in bonds:
        a = abs(total_sum - 2*(sums(i,j)))
        if a < min:
            min = a
    return min
print(main())