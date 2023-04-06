

from collections import deque

def solution(bridge_length, weight, truck_weights):
    ans = 0
    temp = 0
    # 트럭 무게 합(임시 저장 공간)
    bridge_q = deque(bridge_length * [0])
    # 다리의 현재 상태를 저장하기 위한 큐.
    truck_q = deque(truck_weights)
    # 아직 다리를 건너지 않은 트럭들을 저장하기 위한 큐.

    while len(bridge_q):
        ans += 1
        # 1초가 지남.

        temp -= bridge_q[0]
        bridge_q.popleft()
        # 해당 트럭이 다리를 완전히 건너가서 다리를 떠남.
        # 가장 앞 원소 빼내서 총합에서 뺌.

        if truck_q:
        # 만약 truck_q에 아직 남아있는 트럭이 있다면,
            if temp + truck_q[0] <= weight:
                temp += truck_q[0]
                bridge_q.append(truck_q.popleft())
            # 다리 위의 트럭들의 무게 합 + 다음에 건널 트럭의 무게 weight보다 작거나 같다면,
            # 해당 트럭을 다리에 올리고 temp에 더해줌.

            else:
                bridge_q.append(0)
                # 다리 위의 트럭들이 한 칸씩 앞으로 전진하는 것을 의미.
    
    return ans

