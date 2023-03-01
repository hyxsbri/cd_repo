

# Python_힙(heapq 모듈) - 최소힙 사용
# O(logN)
import sys, heapq
input = sys.stdin.readline
# n <= 100,0000 & 한 줄에 하나씩 주어짐 - sys 모듈 활용(빠른 입력)
h = []

for _ in range(int(input())):
    x = int(input())

    if x == 0:
        print(heapq.heappop(h)[1] if len(h) else 0)
        # 단일값이 아닐 시, 선형 구조의 맨 앞 요소부터 우선 비교 후 정렬 및 출력
        # 대소 비교 가능한 모든 자료형 가능 ex. 문자열(a < b) / 클래스 형태는 불가능
        # 절대값 같을 시, 원본값 비교 후 더 작은 값 출력
    else:
        heapq.heappush(h, (abs(x), x))

