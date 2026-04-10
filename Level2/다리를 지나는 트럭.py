from collections import deque

def solution(max_length, bridge_weight, truck_weights):
    answer = 0
    bridge = deque([0] * max_length)
    trucks = deque(truck_weights)
    current_weight = 0 

    while bridge:
        answer += 1
        out = bridge.popleft()
        current_weight -= out

        if trucks:
            if current_weight + trucks[0] <= bridge_weight:
                t = trucks.popleft()
                bridge.append(t)
                current_weight += t
            else:
                bridge.append(0)
                
    return answer