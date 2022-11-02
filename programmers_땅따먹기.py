

def solution(land):
    
    for i in range(1, len(land)):
        for j in range(len(land[0])):
            land[i][j] += max(land[i-1][:j] + land[i-1][j+1:])
            # j 열 빼고 만든 리스트에서 max 값을 뽑아 더해주기
            
    return max(land[-1])

