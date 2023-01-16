

n, m = map(int, input().split())
board = []
cnt = []

for _ in range(n):
    board.append(input())

for a in range(n-7):
    for b in range(m-7):
        first_w = 0
        first_b = 0
        for i in range(a, a+8):
            for j in range(b, b+8):
                if (i+j) % 2 == 0:
                    if board[i][j] != "W":
                        first_w += 1
                    if board[i][j] != "B":
                        first_b += 1
                else:
                    if board[i][j] != "B":
                        first_w += 1
                    if board[i][j] != "W":
                        first_b += 1
        cnt.append(min(first_w, first_b))

print(min(cnt))

