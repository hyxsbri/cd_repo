

n = int(input())
b3 = 0
b5 = 0

b5 += (n // 5)
n -= (5*(n // 5))

if n % 5 != 0: ???

if n % 3 == 0:
    b3 += (n // 3)
    print(b3 + b5)
else:
    print(-1)










