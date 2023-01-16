

# fibonacci

def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x-1) + fibo(x-2)

# Using DP(top down memoization)

d = [0]*100

def fibo2(x):
    # 종료 조건
    if x == 1 or x == 2:
        return 1
    # 계산한 적 있으면 그대로 반환
    if d[x] != 0:
        return d[x]
    d[x] = fibo2(x-1) + fibo2(x-2)
    return d[x]

# bottom up

d[1] = 1
d[2] = 1
n = 99

for i in range(3, n+1):
    d[i] = d[i-1]+d[i-2]

print(d[n])





















