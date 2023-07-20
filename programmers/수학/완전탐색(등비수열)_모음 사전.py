

# https://school.programmers.co.kr/learn/courses/30/lessons/84512

def solution(word):
    ans= 0
    vowels= {'A':0, 'E':1, 'I':2, 'O':3, 'U':4}

    for i, char in enumerate(word):
        offset= sum([5**j for j in range(5- i)])
        ans+= vowels[char] * offset+ 1
        
    return ans







