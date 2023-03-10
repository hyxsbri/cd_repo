

# 활동 선택 문제(Activity Selection Problem)
import sys
input = sys.stdin.readline
meetings = []

for _ in range(int(input())):
    start, end = map(int, input().split())
    meetings.append((end, start))
# meetings = [tuple(map(int, input().split())) for _ in range(int(input()))]

meetings.sort()
# end, start 안 바꾸고 그대로 정렬 시,
# meetings.sort(key = lambda x: (x[1], x[0]))
t = 0
# 기준 시간 t 설정
ans = 0
for end, start in meetings:
    if t <= start:
    # 시작, 종료 시간 같은 회의도 ans에 포함됨
        ans += 1
        t = end
        # 기준 시간 t 갱신

print(ans)





