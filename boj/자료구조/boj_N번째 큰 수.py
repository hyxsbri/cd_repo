

# 우선순위 큐(min-heap) 활용
import heapq
hq = []
n = int(input())

for _ in range(n):
    for i in map(int, input().split()):

        if len(hq) >= n:
            heapq.heappushpop(hq, i)
            # 우선순위 큐가 n 이상일때, 입력값 넣은 후 가장 작은 값 pop 
        else:
            heapq.heappush(hq, i)
            # n 미만일 시, 우선순위 큐에 숫자 삽입

print(heapq.heappop(hq))
# 우선순위 큐에서 pop한 수가 N번째 큰 수

