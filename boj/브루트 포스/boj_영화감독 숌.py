

# 단순 반복문으로 1씩 카운팅 후, 666 이 들어있는지 판별

n = int(input())
name = 666
cnt=0

while True:
    if "666" in str(name):
        cnt+=1
        if cnt == n:
            print(name)
            break
    name+=1

