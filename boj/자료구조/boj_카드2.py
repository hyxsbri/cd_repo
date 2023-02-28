

# 큐 - 상위호환 덱 모듈 활용
from collections import deque

dq = deque()
for i in range(1, int(input())+1):
    dq.append(i)

while len(dq)>1:
    dq.popleft()
    # 제일 위에 있는 카드 제거
    dq.append(dq.popleft())
    # 제일 위에 있는 카드 뒤로 보내기

print(dq.pop())
# 마지막 남은 카드

