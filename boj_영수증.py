

X = int(input())
#영수증에 적힌 총  금액

N = int(input())
#물건 종류 수

total = 0
#실제 구매금액

for _ in range(N):
    a,b = map(int, input().split())
    total += a*b

print('Yes' if X == total else 'No')
#영수증과 일치 시 Yes, 불일치 시 No

