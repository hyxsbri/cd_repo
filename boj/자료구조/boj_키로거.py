

# 덱 활용
from collections import deque

for _ in range(int(input())):
    dq1 = deque() # 커서 왼쪽
    dq2 = deque() # 커서 오른쪽

    for ch in input():
        if ch == '<':
            if len(dq1):
                dq2.appendleft(dq1.pop())
        elif ch == '>':
            if len(dq2):
                dq1.append(dq2.popleft())
        elif ch == '-':
            if len(dq1):
                dq1.pop()
        else:
            dq1.append(ch)
    
    print(''.join(dq1)+''.join(dq2))


# # 스택 활용
# for _ in range(int(input())):
#     stk1 = []
#     stk2 = []

#     for ch in input():
#         if ch == '<':
#             if len(stk1):
#                 stk2.append(stk1.pop())
#         elif ch == '>':
#             if len(stk2):
#                 stk1.append(stk2.pop())
#         elif ch == '-':
#             if len(stk1):
#                 stk1.pop()
#         else:
#             stk1.append(ch)
    
#     print(''.join(stk1)+''.join(reversed(stk2)))

