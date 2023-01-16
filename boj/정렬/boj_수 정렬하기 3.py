

import sys
input = sys.stdin.readline
from collections import Counter
n = int(input())
l = []

for _ in range(n):
    l.append(int(input()))
l.sort()
l_mod = Counter(l).most_common()
print(round(sum(l)/n))
print(l[n//2])
if len(l_mod) > 1:
    if l_mod[0][1] == l_mod[1][1]:
        print(l_mod[1][0])
    else:
        print(l_mod[0][0])
else:
    print(l_mod[0][0])
print(l[-1]-l[0])


