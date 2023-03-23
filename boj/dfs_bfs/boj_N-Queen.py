

# dfs
# lookup 테이블 활용
# PyPy3
N = int(input())
ans = 0
v1 = [False] * N
# 행 방문 체크
v2 = [False] * 2 * N
# 우상향 방문 체크
v3 = [False] * 2 * N
# 좌상향 방문 체크

def dfs(n):
    global ans
    if n == N:
    # N행까지 진행한 경우 성공, ans += 1
        ans += 1
        return
    
    for j in range(N):
        if v1[j] == v2[n+j] == v3[n-j] == False:
            # 열/ 대각선에 퀸 없는 경우,

            v1[j] = v2[n+j] = v3[n-j] = True
            # 방문 체크하고,

            dfs(n+1)
            # 재귀

            v1[j] = v2[n+j] = v3[n-j] = False
            # 초기화

dfs(0)
print(ans)

