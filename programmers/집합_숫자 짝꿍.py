

# https://school.programmers.co.kr/learn/courses/30/lessons/131128

def solution(X, Y):
    ans = []
    for i in (set(X) & set(Y)): # 교집합
        for _ in range(min(X.count(i), Y.count(i))):
            ans.append(i)
            
    # 내림차순 정렬
    ans.sort(reverse=True)

    # 짝꿍이 존재하지 않으면 '-1' 반환
    if len(ans) == 0:
        return '-1'
    
    # 제일 큰 값이 0이먄 '0' 반환
    if ans[0] == '0':
        return '0'
    
    return ''.join(ans)

