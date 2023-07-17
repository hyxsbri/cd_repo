

# https://school.programmers.co.kr/learn/courses/30/lessons/49994

# visited- 방문 경로 저장(중복 제거, set형) / 초기값 (0, 0)
# dx, dy 로 각각 명령에 따른 xy 좌표 변화
# nx, ny에 각각 x, y 좌표에 변화를 더하여 캐릭터의 새로운 위치를 계산
# 이동한 경로가 좌표평면 경계를 넘지 않는 경우 chk
# 처음 걸어본 길인지 확인하고, 처음 걸어본 경우에만 visited 집합에 경로를 추가, ans+= 1
# 위치 업데이트
# 처음 걸어본 길의 개수인 ans 반환

def solution(dirs):
    ans= 0
    visited= set()
    x, y= 0, 0
    dx= {'U': 0, 'D': 0, 'R': 1, 'L': -1}
    dy= {'U': 1, 'D': -1, 'R': 0, 'L': 0}

    for dir in dirs:
        nx, ny= x+ dx[dir], y+ dy[dir]
        if -5<= nx<= 5 and -5<= ny<= 5:
            if (x, y, nx, ny) not in visited and (nx, ny, x, y) not in visited:
                visited.add((x, y, nx, ny))
                visited.add((nx, ny, x, y))
                ans+= 1
            x, y= nx, ny

    return ans

# (x, y, nx, ny) 는 캐릭터가 현재 위치에서 다음 위치로 이동하는 경로를 표현합니다.
# 여기서 x 와 y 는 현재 위치이고, nx 와 ny 는 다음 위치입니다.
# (nx, ny, x, y) 는 역으로 상태를 표현한 것이며, 이는 캐릭터가 경로를 거꾸로 돌아오는 경우에 대비한 코드입니다.

# 조건문에서 현재 위치에서 다음 위치로의 경로와 그 반대 경로 두 가지를 모두 확인합니다.
# 만약 둘 다 방문하지 않은 상태라면 (not in visited) 성립하게 됩니다.
# 이 경우, 즉 처음 걸어본 길인 경우에만 visited 집합에 경로를 추가하고 ans 값을 증가시키게 됩니다.
# 이렇게 함으로써 캐릭터가 처음 지나간 경로에 대해서만 정확하게 계산할 수 있게 됩니다.

