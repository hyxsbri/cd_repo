

# https://school.programmers.co.kr/learn/courses/30/lessons/161990

def solution(wallpaper):
    a, b = [], []
    for i in range(len(wallpaper)): # 행
        for j in range(len(wallpaper[i])): # 각 행의 요소 확인

            if wallpaper[i][j] == '#': # 파일이 존재하면,
                a.append(i) # 행 index
                b.append(j) # 행 안에서의 위치 index

    return [min(a), min(b), max(a)+1, max(b)+1] # 최소 드래그 지점 반환

