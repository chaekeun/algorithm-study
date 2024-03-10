import collections

def solution(bridge_length, weight, truck_weights):
    q = collections.deque([0]*bridge_length)
    truck_weights = collections.deque(truck_weights)
    sec = 0
    total = 0
    
    while q:
        sec += 1
        qq = q.popleft()
        total -= qq
        if truck_weights:
            if total + truck_weights[0]<= weight:
                truck = truck_weights.popleft()
                total += truck
                q.append(truck)
            else:
                q.append(0)
                
    return sec