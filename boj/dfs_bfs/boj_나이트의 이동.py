

# 최단거리 - bfs
from collections import deque

dy = (-1, -2, -2, -1, 1, 2, 2, 1)
dx = (-2, -1, 1, 2, -2, -1, 1, 2)
# 나이트는 총 여덟 방향으로 이동 가능

def is_valid_coord(y, x):
    return 0 <= y < n and 0 <= x < n
# 범위에서 벗어나지 않는지 확인하는 함수를 사전에 정의

for _ in range(int(input())):
    n = int(input())
    dq = deque()
    chk = [[False] * n for _ in range(n)]
    sy, sx = map(int, input().split())
    # 출발지
    ey, ex = map(int, input().split())
    # 목적지

    chk[sy][sx] = True
    # 출발지 방문 체크 배열에 체크
    dq.append((sy, sx, 0))
    # 덱에 추가해서 시작

    while dq:
        y, x, cnt = dq.popleft()
        # 추출

        if y == ey and x == ex:
            print(cnt)
            break
        # while문은 목적지 좌표에 도달하면 멈추고, 이동 횟수를 반환한다.

        for k in range(8):
        # 여덟 방향을 돌면서,
            ny = y + dy[k]
            nx = x + dx[k]
            ncnt = cnt + 1
            if is_valid_coord(ny, nx) and not chk[ny][nx]:
                chk[ny][nx] = True
                dq.append((ny, nx, ncnt))
                # 다시 while문 처음으로 돌아감

