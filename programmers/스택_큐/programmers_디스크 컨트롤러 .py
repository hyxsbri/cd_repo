

# 작업 스케줄링(우선순위 큐)
import heapq

def solution(jobs):
    ans, now, i = 0, 0, 0
    start = -1
    h = []

    while i < len(jobs):
        for j in jobs:

            if start < j[0] <= now:
                heapq.heappush(h, [j[1], j[0]])
                # 작업 시간이 적은 작업부터 우선순위 갖도록, 최소 heap(Python) 활용
                # j[1]: 작업 소요 시간 / j[0]: 작업이 요청되는 시점

        if len(h) > 0:
            current = heapq.heappop(h)
            start = now
            now += current[0]
            # 작업 시간이 가장 작은 
            ans += (now - current[1])
            i += 1
            # 처리된 작업 수 증가

        else:
            now += 1

    return int(ans / len(jobs))

