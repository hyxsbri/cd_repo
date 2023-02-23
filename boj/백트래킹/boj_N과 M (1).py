

from itertools import permutations
# 순열 이용
n, m = map(int, input().split())

arr = [i for i in range(1, n+1)]
for perm in permutations(arr, m):
    print(*perm)

