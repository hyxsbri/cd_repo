

# https://school.programmers.co.kr/learn/courses/30/lessons/133499

def solution(babbling):
    ans = 0
    words=["aya", "ye", "woo", "ma"]
    repeats=["ayaaya", "yeye", "woowoo", "mama"]
    # 안되는 반복 조합

    for b in babbling:
        for r in repeats:
            b = b.replace(r, "X")
        for w in words:
            b = b.replace(w, "O")

        isValid = True

        for char in b:
            if char != "O":
            # b에 포함된 문자열 중에 하나라도 "O" 표시 아니면 안됨
                isValid = False
                break
                # 바로 다음 b로 넘어감 
        if isValid:
            ans += 1
    
    return ans

