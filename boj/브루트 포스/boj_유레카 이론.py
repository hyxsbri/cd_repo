

eureka = []
for i in range(1, 1002):
    a = i*(i+1)//2
    if a <= 1000:
        eureka.append(a)
# 삼각수 미리 계산 후 리스트에 추가

def is_possible(n):
    # 같은 삼각수 선택 가능 -> 3중 for문 활용
    for j in range(len(eureka)):
        for k in range(len(eureka)):
            for m in range(len(eureka)):
                if eureka[j]+eureka[k]+eureka[m] == n:
                    return 1
    else:
        return 0

for _ in range(int(input())):
    print(is_possible(int(input())))

