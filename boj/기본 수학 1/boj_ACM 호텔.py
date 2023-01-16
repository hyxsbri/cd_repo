

t = int(input())

for _ in range(t):

    k = int(input()) # 층수
    n = int(input()) # 호수
    people = [i for i in range(1, n+1)] # 0층의 각 호수에 사는 사람

    for i in range(k):
        new = [] # 0층부터 k-1 층에 사는 사람 수 담는 리스트
        for j in range(n):
            new.append(sum(people[ :j+1]))
        people = new.copy() #갱신
    
    print(people[-1]) # k층 n호에 사는 사람 수



    
