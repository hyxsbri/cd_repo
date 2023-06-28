

# https://school.programmers.co.kr/learn/courses/30/lessons/131127
# from collections import Counter
# update(['']) - 갯수 추가, substract(['']) - 갯수 감소

from collections import Counter

def solution(want, number, discount):
    ans=0
    chk=dict()

    for w, n  in zip(want, number):
        chk[w]=n
    
    for i in range(len(discount)-9): # 회원 자격 부여(10일)
        c = Counter(discount[i:i+10]) # 10일 간 가능 구매내역의 Counter 객체 생성
        if c == chk:
            ans+=1
    
    return ans

