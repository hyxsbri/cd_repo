

# https://school.programmers.co.kr/learn/courses/30/lessons/138476

def solution(k, tangerine):
    cnt=0
    t_dict = {} # count(i) 시간 초과 발생, dict 로 대체
    arr=[]

    for i in tangerine:
        if i in t_dict:
            t_dict[i]+=1
        else:
            t_dict[i]=1
    
    arr = sorted(t_dict.values(),reverse=True)
    # 내림차순 정렬

    for j in arr:
        if k<=j:
            cnt+=1
            break
        else:
            cnt+=1
            k -= j
    
    return cnt

