def array_left_rotation(a, n, k):
   k = k%n
   a.append(a[0:k])
   a = a[k:]
   return a


n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, k);
print(*answer, sep=' ')