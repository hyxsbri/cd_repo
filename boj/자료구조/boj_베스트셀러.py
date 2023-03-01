

# map 구조는 dict로 구현 - (key, value) 형태 like JSON
# O(1), 해시 구조
books = dict()

for _ in range(int(input())):
    name = input()

    if name in books:
        books[name] += 1
        # 이미 존재할 시, 갯수 추가
    else:
        books[name] = 1

max_val = max(books.values())
# 가장 높은 갯수
arr = []

for k, v in books.items():
    if v == max_val:
        arr.append(k)

print(sorted(arr)[0])
# max_val 여러개 시, key 오름차순 정렬 후 가장 첫 책 제목

