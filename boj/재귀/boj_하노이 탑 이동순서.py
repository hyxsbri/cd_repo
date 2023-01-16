
# 원판이 1개밖에 없는 경우 > 3번 기둥으로 옮기고 끝.
# 가장 큰 원판을 제외한 나머지 원판을 2번기둥으로 옮긴다.
# 가장 큰 원판을 3번 기둥으로 옮긴다.
# 나머지 원판들을 3번기둥으로 옮긴다.

def hanoi(num, start, end):
    if num == 1:
        print(start, end)
        return
    else:
        hanoi(num-1, start, 6-start-end)
        print(start, end)
        hanoi(num-1, 6-start-end, end)

N = int(input())

print(2**N -1)
hanoi(N, 1, 3)
