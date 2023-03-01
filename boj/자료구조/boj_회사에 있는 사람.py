

# 집합 set - 중복 x
# O(1), 해시 구조
import sys
input = sys.stdin.readline
s = set()

for _ in range(int(input())):
    name, el = input().split()

    if el == 'enter':
        s.add(name)
        # 집합에 이름 추가(add)
    else:
        # el == 'leave'
        if name in s:
            s.remove(name)
            # 집합에 이름 제거(remove)

# 출근한 사람 이름만 set에 남게 됨

for name in sorted(s, reverse=True):
    # 사전 역순(내림차순)으로 출력
    print(name)

