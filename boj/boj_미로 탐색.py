

# 최단거리 - bfs 사용
# 다음 진행 칸을 알아볼 때, 그 칸이 갈 수 있는 칸인지 검사
from collections import deque

dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)

n, m = map(int, input().split())
board = [input() for _ in range(n)]
chk = [[False] * m for _ in range(n)]
# 방문 체크 필수, 하지 않으면 이미 지나온 곳 다시 방문
dq = deque()

dq.append((0, 0, 1))
chk[0][0] = True
# 초기 시작점 설정/ y, x 외에 거리 d도 같이 큐에 저장

def is_valid_coord(y, x):
    return 0 <= y < n and 0 <= x < m

while len(dq) > 0:
    y, x, d = dq.popleft()

    if y == n-1 and x == m-1:
        print(d)
        break
    # 답 찾으면 거리 d 출력 후, while문 종료

    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        nd = d+1
        if is_valid_coord(ny, nx) and board[ny][nx] == '1' and not chk[ny][nx]:
            chk[ny][nx] = True
            dq.append((ny, nx, nd))

