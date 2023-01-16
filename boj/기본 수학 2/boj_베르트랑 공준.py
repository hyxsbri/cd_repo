
import sys
input = sys.stdin.readline
def prime(k):
    if k == 1:
        return 0
    for i in range(2, int(k**0.5)+1):
        if k % i == 0:
            return 0
    return 1

T = int(input())
for _ in range(T):
    n = int(input())
    a, b = n//2, n//2
    while a > 1:
        if prime(a) and prime(b):
            print(a, b)
            break
        else:
            a -= 1
            b += 1


