

# https://school.programmers.co.kr/learn/courses/30/lessons/133502

def solution(ingredient):
    cnt=0
    burger=[]
    # burger = [1,2,3,1] (빵, 야채, 고기, 빵)

    for i in ingredient:
        burger.append(i)
        if burger[-4:]==[1,2,3,1]:
        # 재료가 append 될 때마다 수시 확인
            cnt+=1
            for _ in range(4):
                burger.pop()
            # del burger[-4:]도 가능
    
    return cnt

