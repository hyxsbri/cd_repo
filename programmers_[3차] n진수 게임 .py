
# 진수 변환
def conv(num, n):
    txt = '0123456789ABCDEF'
    quot, remain = divmod(num, n)
    return conv(quot, n) + txt[remain] if quot else txt[remain]

# 튜브의 인덱스 리스트
def tube_idx(m, p, idx_max):
    idx = [i for i in range(p - 1, idx_max, m)]
    return idx

def solution(n, t, m, p):
    ans = ''
    converted = '' # n진수로 변환되어 쭉 나열된 str
    idx_max = m * t # 튜브의 마지막 인덱스
    
    # 최종 인덱스 범위까지 포함하는 converted
    i = 0
    while len(converted) - 1 < idx_max:
        converted += conv(i, n)
        i += 1
    
    # 튜브가 말하는 인덱스
    idx = tube_idx(m, p ,idx_max)
    
    # 튜브의 순서에 맞는 것만 ans 에 추가
    for i in idx:
        ans += converted[i]
    
    return ans
