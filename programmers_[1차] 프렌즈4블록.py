

def solution(m, n, board):
    from collections import deque   
    ans = 0
    chk = set()
    board = [list(i) for i in board]

    # 2*2 블록 조건에 맞으면 집합에 해당 index 추가
    def boom(b):
        for i in range(m-1):
            for j in range(n-1):
                if b[i][j] == b[i+1][j] == b[i][j+1] == b[i+1][j+1] != '0':
                    chk.add((i,j))
                    chk.add((i+1,j))
                    chk.add((i,j+1))
                    chk.add((i+1,j+1))
    
    #격자를 재배열하는 함수
    def arrange(b):
        for j in range(len(b[0])):
            q = deque([])
            
            for i in range(len(b)-1, -1, -1):
                if b[i][j] == '0':
                    q.append((i,j))
                else:
                    if q:
                        qi, qj = q.popleft()
                        b[qi][qj] = b[i][j]
                        b[i][j] = '0'
                        q.append((i,j))
    
    while True:
        boom(board)
        if chk:
            for i, j in chk:
                board[i][j] = '0'
            ans += len(chk)
            arrange(board)
            chk.clear()
        else:
            break
    
    return ans
    
     