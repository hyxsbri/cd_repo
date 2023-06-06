

# https://school.programmers.co.kr/learn/courses/30/lessons/136798
# 약수를 구하면 항상 그 짝이 되는 수가 존재한다(ex. 6=2x3)

def solution(number, limit, power):
    ans = 0
    knight=[]
    divisor_knight=[]

    # 기사 번호 담은 배열
    for i in range(number):
        knight.append(i+1)

    # 각 기사 번호별 약수 담은 배열
    for k in knight:
        tmp=[]
        for i in range(1, int(k**0.5)+1):
            if k%i == 0:
                tmp.append(i)
                if((i**2) != k):
                    # 항상 그 짝이 되는 수가 존재한다(같은 수의 제곱 수 중복값 제외).
                    tmp.append(k//i)
        divisor_knight.append(len(tmp))
    
    for d in divisor_knight:
        if d<=limit:
            ans += d
        else:
            ans += power

    return ans

