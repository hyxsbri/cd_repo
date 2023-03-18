

from collections import deque

dy = (0, 1, 0, -1)
dx = (-1, 0, 1, 0)
n = int(input())
chk = [[False]*n for _ in range(n)]

def is_valid_coord(y, x):
    return 0 <= y < n and 0 <= x < n

def dfs(y, x):
    if adj[y][x] == ans:
        return
    
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if is_valid_coord(ny, nx) and not chk[ny][nx]:
            chk[ny][nx] = True
            dfs(ny, nx)
            # dfs - 재귀 호출

def bfs(sy, sx):
    q = deque()
    chk[sy][sx] = True
    q.append((sy, sx))

    while len(q):
        y, x = q.popleft()
        if adj[y][x] == ans:
            return
        # bfs - while loop 순환 중 중간에 답 찾으면 return
        
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if is_valid_coord(ny, nx) and not chk[ny][nx]:
                chk[ny][nx] = True
                q.append(ny, nx)

