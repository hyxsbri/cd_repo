

def solution(skill, skill_trees):
    cnt = 0
    for tree in skill_trees:
        s = ''
        # 스킬 트리 돌 때 마다 s 초기화
        for i in tree:
            if i in skill:
                s += i
                # i가 스킬을 포함하면 s 에 추가
        if skill[:len(s)] == s:
            cnt += 1
            # s 가 스킬 트리 순서와 일치하면 cnt + 1
    return cnt

