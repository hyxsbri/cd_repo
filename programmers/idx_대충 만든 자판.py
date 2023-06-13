

# https://school.programmers.co.kr/learn/courses/30/lessons/160586

def solution(keymap, targets):
    ans = []

    for word in targets:
        times = 0

        for char in word:
            flag = False
            # False 값으로 기본 설정
            time = 101
            # index 최대값에 대한 키 누른 횟수 설정

            for key in keymap:
                if char in key:
                    time = min(key.index(char)+1, time)
                    # 알아서 최소값으로 갱신되게끔, time = min(key.index(char)+1, time)
                    flag = True
            
            if not flag:
                # flag = False 라는건 유효하지 않은 값이 있다는 뜻
                times = -1
                # -1 설정
                break
            times += time
        
        ans.append(times)

    return ans

