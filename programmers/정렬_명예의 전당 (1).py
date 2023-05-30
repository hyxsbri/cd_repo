


# https://school.programmers.co.kr/learn/courses/30/lessons/138477

def solution(k, score):
    ans = []
    top_k = []
    
    for s in score:
        top_k.append(s)
        top_k = sorted(top_k, reverse = True)[:k]
        
        ans.append(min(top_k))
        
    return ans


