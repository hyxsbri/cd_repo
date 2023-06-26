

# https://school.programmers.co.kr/learn/courses/30/lessons/131701
# 연속 부분 수열 합 개수 = 이중 for문으로 풀이
elements=[7,9,1,1,4]

def solution(elements):
    ans = set()
    # 집합 자료형으로 중복 수열 합 제거
    # 슬라이싱은 인덱스 초과 오류 나지 않음(Python)

    element_len = len(elements)
    elements = 2*elements

    for i in range(element_len):
        for j in range(element_len):
            ans.add(sum(elements[i:i+j+1]))
    
    return len(ans)

