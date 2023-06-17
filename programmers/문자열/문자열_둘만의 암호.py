

# https://school.programmers.co.kr/learn/courses/30/lessons/155652

def solution(s, skip, index):
    ans = ''
    alpha='abcdefghijklmnopqrstuvwxyz' # 알파벳 전체

    for ch in skip: # skip의 문자 하나하나
        if ch in alpha:
            alpha=alpha.replace(ch,'') # 제외

    for i in s: # s의 문자 하나하나
        change = alpha[(alpha.index(i)+index)%len(alpha)] # alpha에서의 인덱스+추가 인덱스(순환 고려)
        ans += change
    
    return ans

