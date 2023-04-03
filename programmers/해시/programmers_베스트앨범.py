

# 해시 알고리즘 in Python - 딕셔너리 사용

def solution(genres, plays):
    ans = []

    dic1 = {}
    dic2 = {}

    for i, (g, p) in enumerate(zip(genres, plays)):
        if g not in dic1:
            dic1[g] = [(i, p)]
        else:
            dic1[g].append((i, p))

        if g not in dic2:
            dic2[g] = p
        else:
            dic2[g] += p
        
    for (k, v) in sorted(dic2.items(), key=lambda x:x[1], reverse=True):
    # 속한 노래가 많이 재생된 장르를 먼저 수록
        for (i, p) in sorted(dic1[k], key=lambda x:x[1], reverse=True)[:2]:
        # 장르 내에서 많이 재생된 노래를 먼저 수록
        # 장르 내에서 재생 횟수가 같은 노래 중, 고유 번호가 낮은 노래를 먼저 수록
        # 장르 별로 가장 많이 재생된 노래를 두 개씩 모음[:2]
            ans.append(i)
    
    return ans
    # dic에 items() 메서드를 사용해주면 {key : value}의 형태를 [(key, value)]의 형태로
    # value값으로 정렬하려면 lambda 사용

