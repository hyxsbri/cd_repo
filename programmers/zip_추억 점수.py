

# https://school.programmers.co.kr/learn/courses/30/lessons/176963

def solution(name, yearning, photo):
    ans = []
    score = {n:y for n,y in zip(name, yearning)}
    temp = 0
    
    for j in photo:
        for k in j:
            if k in score.keys():
                temp += score[k]
        ans.append(temp)
        temp = 0
        
    return ans

