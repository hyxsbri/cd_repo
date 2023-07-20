

# https://school.programmers.co.kr/learn/courses/30/lessons/154539

num1= [2, 3, 3, 5]
num2= [9, 1, 5, 3, 6, 2]

def solution(numbers):
    stk= []
    ans= [-1] * len(numbers)

    for i, num in enumerate(numbers):
        while stk and numbers[stk[-1]] < num:
            j= stk.pop()
            ans[j]= num

        stk.append(i)
        # while문 False 일때, idx 저장

    return ans

