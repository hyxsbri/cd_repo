


arr = [[0 for _ in range(101)] for _ in range(101)]
n = int(input())
ans = 0

for _ in range(n):
    a, b = map(int, input().split())

    for i in range(a, a+10):
        for j in range(b, b+10):
            arr[i][j] = 1

for k in arr:
    ans += sum(k)

print(ans)




