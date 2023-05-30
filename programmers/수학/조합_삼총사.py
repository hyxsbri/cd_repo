

from itertools import combinations
# 조합(순서에 의미 없음, 같은 값이 뽑히면 같은 경우의 수)

def solution(number):
    ans = 0
    for i in list(combinations(number, 3)):
        if sum(i) == 0:
        # 세 개의 합이 0이 되는 경우의 수를 찾으면 횟수 1 증가
            ans+=1
        
    return ans

