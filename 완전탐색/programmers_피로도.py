

def solution(k, dungeons):
    from itertools import permutations
    # 어떤 던전을 먼저 도는지 순서가 필요하므로 permutations 사용
    answers = []

    for l in permutations(dungeons, len(dungeons)):
        remain, cnt = k, 0
        #피로도, 횟수 순열마다 초기화
        for i, j in l:
            if (remain >= i):
                remain -= j
                #피로도 차감
                cnt += 1
                #탐험 횟수 +1
        answers.append(cnt)
    return max(answers)
    #순열들에서 나온 cnt 값 중 가장 큰 값 return

    