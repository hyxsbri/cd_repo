




board = [list(map(int, input().split())) for _ in range(9)]
l = []

for i in range(9):
    l.append(max(board[i]))

print(max(l))

for j in range(9):
    for k in range(9):
        if max(l) == board[j][k]:
            print(j+1, k+1)





























