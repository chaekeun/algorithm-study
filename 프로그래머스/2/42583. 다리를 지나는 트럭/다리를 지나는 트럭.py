from collections import deque

def solution(bridge_length, weight, truck_weights):
    current, answer = 0,0
    bridge = deque([0]*bridge_length)
    truck_weights = deque(truck_weights)
    
    while bridge:
        answer += 1
        current -= bridge.popleft()
        if truck_weights:
            if current+truck_weights[0]<=weight:
                truck = truck_weights.popleft()
                bridge.append(truck)
                current += truck
                
            else:
                bridge.append(0)
                
    return answer