

# n, m = map(int, input().split())
# arr = []

# for _ in range(n):
#     arr.append(str.lower(input()))

# for _ in range(m):
#     a = input()
#     if a.isalpha():
#         print(arr.index(str.lower(a))+1)
#     else:
#         print(str.capitalize(arr[int(a)-1]))


import sys

n, m = map(int, input().split())
int_key = {}
name_key = {}
for i in range(n):
    name = sys.stdin.readline().strip()
    int_key[i] = name
    name_key[name] = i

for _ in range(m):
    value = sys.stdin.readline().strip()
    if value.isdigit():
        print(int_key[int(value)-1])
    else:
        print(name_key[value]+1)

