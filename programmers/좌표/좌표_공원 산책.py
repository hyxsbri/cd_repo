

# https://school.programmers.co.kr/learn/courses/30/lessons/172928

def solution(park, routes):
    # 위치 index
    x=0
    y=0

    # 시작 위치 index 찾기
    for i in range(len(park)):
        for j in range(len(park[i])): # 직사각형 모양의 격자
            if park[i][j]=='S':
                x=j
                y=i # 리스트 표현(행 x 열) /좌표 표현 방식(열 x 행)
                    # 서로 다름
                break
        
    # 이동
    for r in routes:
        # 위치 초기화
        nx=x
        ny=y

        # 공원 밖 나갈 시 or 장애물 존재할 때 명령 무시
        for step in range(int(r[2])):
            # 동쪽
            if r[0]=='E' and nx!=len(park[0])-1 and park[ny][nx+1]!='X':
                nx += 1
                if step == int(r[2])-1:          
                    x = nx # step 만큼 움직였으면, 위치 갱신
            
            # 서쪽
            elif r[0]=='W' and nx!=0 and park[ny][nx-1]!='X':
                nx -= 1          
                if step == int(r[2])-1:          
                    x = nx
            
            # 남쪽
            elif r[0]=='S' and ny!=len(park)-1 and park[ny+1][nx]!='X':
                ny += 1          
                if step == int(r[2])-1:          
                    y = ny

            # 북쪽
            elif r[0]=='N' and ny!=0 and park[ny-1][nx]!='X':
                ny -= 1
                if step == int(r[2])-1:          
                    y = ny
        
    return [y, x] # 좌표 표현 방식으로 출력

