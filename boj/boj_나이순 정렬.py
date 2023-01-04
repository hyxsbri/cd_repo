

n = int(input())
l = []

for i in range(n):
    [a,b] = input().split()
    l.append([int(a),i, b])

l.sort()

for j in range(n):
    print(l[j][0], l[j][2])






