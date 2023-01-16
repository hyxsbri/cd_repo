

std = [i for i in range(1, 31)]
for _ in range(28):
    a = int(input())
    std.remove(a)
    #30명 중 과제 제출한 학생 번호 제거

std.sort()
#작은 학생 번호부터 출력
print(std[0])
print(std[1])

