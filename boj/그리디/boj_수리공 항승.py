

coord = [False]*1001
n, l = map(int, input().split())
for i in map(int, input().split()):
    coord[i] = True
    # 물 새는 구멍에 true 표시

ans = 0
x = 0
while x <= 1000:
    if coord[x]:
        ans += 1
        x += l
        # 테이프 길이만큼 skip
    else:
        x += 1

print(ans)

