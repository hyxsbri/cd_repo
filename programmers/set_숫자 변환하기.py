

# https://school.programmers.co.kr/learn/courses/30/lessons/154538

def solution(x, y, n):
    ans = 0
    s = set()
    s.add(x)

    while s:
        if y in s:
            return ans
        
        nxt = set()
        for i in s:
            if i+n <= y:
                nxt.add(i+n)
            if i*2 <= y:
                nxt.add(i*2)
            if i*3 <= y:
                nxt.add(i*3)
        s = nxt
        ans += 1
    
    return -1



