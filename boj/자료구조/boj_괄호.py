

# 스택 - FILO / LIFO
for _ in range(int(input())):
    stk = []
    ans = 'YES'
    for c in input():
        if c == '(':
            stk.append(c)
            # 여는 괄호는 스택에 삽입
        else:
            # 닫는 괄호일 시,
            if len(stk)>0:
                stk.pop()
                # 여는 괄호 남아있으면 스택에서 삭제
            else:
                ans = 'NO'
                # 남아있지 않으면 NO
    if len(stk)>0:
        ans = 'NO'
        # 모든 작업 완료 후 여는 괄호 남아있으면 NO
    
    print(ans)

