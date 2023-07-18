

maps1= [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
maps2= [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]
# https://school.programmers.co.kr/learn/courses/30/lessons/1844


from collections import deque
def solutions(maps):
    n= len(maps)
    m= len(maps[0])
    visited= [[-1 for _ in range(m)] for _ in range(n)]

    dx= [-1, 1, 0, 0]
    dy= [0, 0, -1, 1]

    def bfs(x, y):
        q= deque([(x, y)])
        visited[x][y]= 1
        while q:
            x, y= q.popleft()
            for i in range(4):
                nx, ny= x+ dx[i], y+ dy[i]
                if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1 and visited[nx][ny] == -1:
                    visited[nx][ny]= visited[x][y]+ 1
                    q.append((nx, ny))
    bfs(0, 0)
    return visited[n-1][m-1]

print(solutions(maps1))
print(solutions(maps2))

