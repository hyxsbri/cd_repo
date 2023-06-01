

# https://school.programmers.co.kr/learn/courses/30/lessons/159994

def solution(cards1, cards2, goal):
    ans = 'Yes'
    idx1, idx2 = 0, 0

    for word in goal:
        if len(cards1)>idx1 and word == cards1[idx1]:
            idx1 += 1
        elif len(cards2)>idx2 and word == cards2[idx2]:
            idx2 += 1
        else:
            ans = 'No'
            break

    return ans    
    
