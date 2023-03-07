

N= int(input())
board = [list(input()) for _ in range(N)]
ans = 1

def search():
    global ans
    for i in range(N):
        cnt = 1
        for j in range(1, N):
            if board[i][j-1] == board[i][j]:
            # 전 행이랑 사탕색 같으면 cnt 증가
                cnt += 1
                ans = max(ans, cnt)
            else:
                cnt = 1
    
    for j in range(N):
        cnt = 1
        for i in range(1, N):
            if board[i-1][j] == board[i][j]:
            # 전 열이랑 사탕색 같으면 cnt 증가
                cnt += 1
                ans = max(ans, cnt)
            else:
                cnt = 1

for i in range(N):
    for j in range(N):
        if j+1 < N:
        # 인덱스 범위 안에서 행 교체 다 해보기
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
            search()
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
            # 원상 복구

        if i+1 < N:
        # 인덱스 범위 안에서 열 교체 다 해보기
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
            search()
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
            # 원상 복구

print(ans)

