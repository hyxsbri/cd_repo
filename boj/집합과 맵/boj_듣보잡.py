

n, m = map(int, input().split())
d = set()
b = set()

for _ in range(n):
    d.add(input())
for _ in range(m):
    b.add(input())

print(len(sorted(d&b)))
for i in sorted(d&b):
    print(i)

# set.add
# set1 & set2, set1.intersection(set2)
#  set1 | set2, set1.union(set2)
# set1 - set2, set1.difference(set2)

