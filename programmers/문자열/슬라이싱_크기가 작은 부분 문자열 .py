

# 숫자로 이루어진 문자열 t와 p가 주어질 때 t에서 p와 길이가 같은 부분 문자열 중에서,
# 부분 문자열이 나타내는 수가 p가 나타내는 수보다 작거나 같은 것이 나오는 횟수를
# return하는 함수 solution을 완성하세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/147355

def solution(t, p):
    ans = 0
    t_len = len(t)
    p_len = len(p)
    p = int(p)

    for i in range(0, t_len-p_len+1):
        if int(t[i:i+p_len])<=p:
            ans+=1

    return ans

