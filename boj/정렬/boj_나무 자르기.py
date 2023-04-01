

# 파라메트릭 서치(이분탐색 활용)
n, m = map(int, input().split())
tree = list(map(int, input().split()))
lo = 0
# 절단기 최소 높이 - 주어진 나무들의 모든 길이를 전부 얻을 수 있음
hi = max(tree)
# 절단기 최대 높이일때, 얻을 수 있는 나무 길이 = 0
mid = (lo+hi)//2

def get_total_tree(h):
# 절단기 높이 정해지면 얻을 수 있는 나무 길이 구하는 함수
    ret = 0
    for t in tree:
        if t > h:
            ret += t-h
    return ret

ans = 0
while lo <= hi:
    if get_total_tree(mid) >= m:
        ans = mid
        lo = mid+1
        # 절단기 높이가 mid 이하도 모두 m 이상의 길이 구할 수 있기 때문에, 최댓값을 찾기 위해 
    else:
        hi = mid-1
    mid = (lo+hi)//2

print(ans)

