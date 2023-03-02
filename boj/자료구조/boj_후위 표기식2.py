

# 스택 활용
n = int(input())
s = input()
val = []
stk = []
for _ in range(n):
    val.append(int(input()))

for ch in s:

    if ch.isalpha():
        stk.append(val[ord(ch)-ord('A')])
        # 스택에 알파벳에 대응되는 숫자 추가
    else:
        b = stk.pop()
        a = stk.pop()
        # 스택이므로 연산 순서에 유의

        if ch == '+':
            stk.append(a+b)
        elif ch == '-':
            stk.append(a-b)
        elif ch == '*':
            stk.append(a*b)
        elif ch == '/':
            stk.append(a/b)

print(f'{stk[0]:.2f}')
# 소수 둘째자리까지 출력
# f-string 소수 둘째자리 = f'{~~~:.2f}'

