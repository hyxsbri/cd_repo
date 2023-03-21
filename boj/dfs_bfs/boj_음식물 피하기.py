

# dfs
import sys
sys.setrecursionlimit(10**6)
# dfs 특

dy = (0, -1, 0, 1)
dx = (-1, 0, 1, 0)

n, m, k = map(int, input().split())
board = [['.'] * m for _ in range(n)]
for _ in range(k):
    y, x = map(int, input().split())
    board[y-1][x-1] = '#'

visited = [[False] * m for _ in range(n)]
sz = 0
ans = 0

def is_valid_coord(y, x):
    return 0 <= y < n and 0 <= x < m

def dfs(y, x):
    global ans, sz
    # 전역 변수로 설정

    visited[y][x] = True
    sz += 1
    ans = max(ans, sz)
    # 더 큰 크기 나올때마다 갱신

    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if is_valid_coord(ny, nx) and not visited[ny][nx] and board[ny][nx] == '#':
            dfs(ny, nx)
            # 유효한 값이면 dfs로 상하좌우 인접한 음식물 탐색

for i in range(n):
    for j in range(m):
        if not visited[i][j] and board[i][j] == '#':
            # 시작
            sz = 0
            dfs(i, j)
            # 음식물을 발견할 때마다 크기 초기화 & dfs

print(ans)

