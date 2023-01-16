




n = int(input()) # 분해합을 입력값으로 받음

for i in range(1, n+1):
    num = sum(map(int, str(i))) # i 의 각 자리 수 합
    num_sum = num + i # 분해합 = 생성자 + 각 자릿수의 합
    if num_sum == n:
        print(i)
        break
    if i == n: # 생성자 i와 입력값이 같다는 것은 생성자가 없다는 뜻
        print(0)








