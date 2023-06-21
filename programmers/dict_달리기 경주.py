

# https://school.programmers.co.kr/learn/courses/30/lessons/178871

def solution(players, callings):
    player_dict = {p:i for i,p in enumerate(players)}
    idx_dict = {i:p for i,p in enumerate(players)}

    for c in callings:
        cur_idx = player_dict[c] # current index(현재 인덱스)
        front_idx = cur_idx-1 # 바로 앞 인덱스

        cur_player = c # 현재 해설진에게 불린 선수 이름
        front_player = idx_dict[front_idx] # 바로 앞 선수 이름

        player_dict[cur_player], player_dict[front_player]=\
        front_idx, cur_idx # player_dict 숫자 값 교체

        idx_dict[cur_idx], idx_dict[front_idx] =\
        front_player, cur_player # idx_dict 선수 이름 교체

    return list(idx_dict.values())

