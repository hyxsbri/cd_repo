

import sys
input = sys.stdin.readline
inf = int(1e9) # 무한을 의미하는 값으로 10억 설정

n, m = map(int, input().split())
# 노드 갯수, 간선 갯수
start = int(input())
# 시작 노드 번호 입력받기

# 이중 리스트 형태 생성
graph = [[] for _ in range(n+1)]
# 방문 체크 리스트
visited = [False]*(n+1)
# 최단 거리 테이블을 inf 로 초기화
dist = [inf]*(n+1)

for _ in range(m):
    a,b,c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c
    graph[a].append((b,c))

# 방문하지 않은 노드 중, 가장 거리가 짧은 노드의 번호를 반환

def small_node():
    min_value = inf
    idx = 0
    for i in range(1, n+1):
        if dist[i] < min_value and not visited[i]:
            min_value = dist[i]
            idx = i
    return idx

# 다익스트라 알고리즘
def dijk(start):
    dist[start] = 0
    visited[start] = True
    for j in graph[start]:
        dist[j[0]] = j[1]

    for _ in range(n-1):
        now = small_node()
        visited[now] = True
        for k in graph[now]:
            cost = dist[now] + k[1]
            if cost < dist[k[0]]:
                dist[k[0]] = cost

dijk(start)

for i in range(1, n+1):
    if dist[i] == inf:
        print('INFINITY')
    else:
        print(dist[i])


# 오름차순 힙 정렬

import heapq
def heapsort(iterable):
    h = []
    ans = []
    for val in iterable:
        heapq.heappush(h, val)
    for i in range(len(h)):
        ans.append(heapq.heappop(h))
    return ans

# 플로이드 워셜

n = int(input())
m = int(input())
graph = [[inf]*(n+1) for _ in range(n+1)]

for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a][b] = c

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, n+1):
        for b in range(1, n+1):
            if graph[a][b] == 1e9:
                print('INFINITY', end = ' ')
            else:
                print(graph[a][b], end = ' ')


