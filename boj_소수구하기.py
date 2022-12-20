
import sys
input = sys.stdin.readline

def prime(k):
    if k == 1:
        return 0
    
    for i in range(2, int(k**0.5)+1):
        if k % i == 0:
            return 0
    return 1

list = []
for i in range(2, 123456*2+1):
    if prime(i):
        list.append(i)

while True:
    n = int(input())
    cnt = 0
    if n == 0:
        break

    for j in list:
    
        if n < j <= 2*n:
            cnt += 1
    print(cnt)



































