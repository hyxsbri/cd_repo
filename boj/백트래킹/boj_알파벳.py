

# bfs 방식 백트래킹
from collections import deque

dy = (0, -1, 0, 1)
dx = (-1, 0, 1, 0)

r, c = map(int, input().split())
board = [input() for _ in range(r)]
chk = [[set() for _ in range(c)] for _ in range(r)]
# 지나온 알파벳 문자열을 집합에 저장, 또 나오면 탐색 x
ans = 0

def is_valid_coord(y, x):
    return 0 <= y < r and 0 <= x < c

dq = deque()
chk[0][0].add(board[0][0])
dq.append((0, 0, board[0][0]))
# 초기값 설정
while dq:
    y, x, s = dq.popleft()
    ans = max(ans, len(s))

    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if is_valid_coord(ny, nx) and board[ny][nx] not in s:
            ns = s + board[ny][nx]
            if ns not in chk[ny][nx]:
                chk[ny][nx].add(ns)
                dq.append((ny, nx, ns))

print(ans)

