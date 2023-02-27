

n, k = map(int, input().split())

arr = [i for i in range(1, n+1)]
pt = 0
ans = []

for _ in range(n):
    pt += k-1
    pt %= len(arr)
    ans.append(arr.pop(pt))

print(f"<{', '.join(map(str, ans))}>")
# f-string - 중괄호 안에 변수명이나 식을 넣어서 원하는 출력 형식 만듦

