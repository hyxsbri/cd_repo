

# https://school.programmers.co.kr/learn/courses/30/lessons/17686

# 파일명은 우선 HEAD 부분을 기준으로 사전 순으로 정렬한다.
# 이때, 문자열 비교 시 대소문자 구분을 하지 않는다. MUZI와 muzi, MuZi는 정렬 시에 같은 순서로 취급된다.

# 파일명의 HEAD 부분이 대소문자 차이 외에는 같을 경우, NUMBER의 숫자 순으로 정렬한다.
# 9 < 10 < 0011 < 012 < 13 < 014 순으로 정렬된다.
# 숫자 앞의 0은 무시되며, 012와 12는 정렬 시에 같은 같은 값으로 처리된다.

# 두 파일의 HEAD 부분과, NUMBER의 숫자도 같을 경우, 원래 입력에 주어진 순서를 유지한다.
# MUZI01.zip과 muzi1.png가 입력으로 들어오면, 정렬 후에도 입력 시 주어진 두 파일의 순서가 바뀌어서는 안 된다.

import re

def solution(files):
    a= sorted(files, key= lambda file: int(re.findall('\d+', file)[0]))
    b= sorted(a, key= lambda file: re.split('\d+', file.lower())[0])

    return b

