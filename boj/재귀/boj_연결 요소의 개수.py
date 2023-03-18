

# dfs
import sys

sys.setrecursionlimit(10**6)
# Python은 재귀호출 횟수가 1,000회로 제한돼있어 늘려줌
input = sys.stdin.readline
n,m = map(int, input().split())

adj = [[False]*(n+1) for _ in range(n+1)]
# 노드 번호가 1부터 시작
for _ in range(m):
# 간선 입력값
    a, b = map(int, input().split())
    adj[a][b] = True
    adj[b][a] = True
    # 무방향(양방향) 그래프

ans = 0
chk = [False] * (n+1)
# 노드 방문 체크 배열 초기화

def dfs(i):
    for j in range(1, n+1):
    # 노드 번호가 1부터 시작
        if adj[i][j] and not chk[j]:
            chk[j] = True
            dfs(j)

for i in range(1, n+1):
# 노드 번호가 1부터 시작
    if not chk[i]:
        ans += 1
        chk[i] = True
        dfs(i)

print(ans)

