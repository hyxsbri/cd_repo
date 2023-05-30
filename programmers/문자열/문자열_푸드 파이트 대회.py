

# https://school.programmers.co.kr/learn/courses/30/lessons/134240

def solution(food):
    ans = ''

    for i in range(1, len(food)):
        ans += str(i)*(food[i]//2)
    temp = ''.join(reversed(list(ans)))

    return ans+'0'+temp


