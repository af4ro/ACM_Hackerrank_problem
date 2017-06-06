import collections
n , m = input().strip().split()
d = collections.defaultdict(list)
for i in range(int(n)):
    a,b = input().strip().split()
    d[a].append(b)
words = [input().split() for j in range(int(m))]

visited = set()
def found(ch):
    result = set(d[ch])
    for i in d[ch]:
        if i not in visited:
            visited.add(i)
            result = result.union(found(i))
    return result

def do(a,b):
    if a == b:
        print('yes')
        return
    if len(a) != len(b):
        print('no')
        return
    for j in range(len(a)):
        visited = set(a[j])
        temp = found(a[j])
        print(temp)
        if b[j] not in temp:
            print('no')
            return
    print('yes')
    return

for i in words:
    do(i[0],i[1])