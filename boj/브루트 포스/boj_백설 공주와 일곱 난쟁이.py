

# 조합 활용
# 기본 정렬 함수 - O(NlogN)
from itertools import combinations
arr = []
for _ in range(9):
    arr.append(int(input()))

for i in combinations(arr, 7):
    if sum(i) == 100:
        for j in i:
            print(j)

## 간소화
# for i in combinations([int(input()) for _ in range(9)], 7):
#     if sum(i) == 100:
#         for j in sorted(i):
#             print(j)
#         break

## 숫자 합 미리 구해두고, 2중 for문으로 두 수를 골라 빼기 
# h = [int(input()) for _ in range(9)]
# tot = sum(h)

# def solve():
#     for i in range(8):
#         for j in range(i+1, 9):
#             if tot - h[i] - h[j] == 100:
#                 for k in h:
#                     if k != h[i] and k != h[j]:
#                         print(k)
#                 return

# solve()

