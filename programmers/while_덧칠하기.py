

# https://school.programmers.co.kr/learn/courses/30/lessons/161989
# pop(0) - 리스트의 첫번째 요소 제거
# popleft() - deque의 맨 왼쪽 요소 제거

def solution(n, m, section):
    ans = 0

    # section에 값이 있다면 반복문 시행
    while section:

        # section의 첫 값에 m을 더한 값 저장
        e = section[0]+m

        # section이 존재하고, section의 첫 값이 e보다 작다면 반복문 시행
        while section and section[0]<e:

            # section의 첫 값을 삭제
            section.pop(0)
        
        # ans에 1을 더함
        ans += 1

    return ans

