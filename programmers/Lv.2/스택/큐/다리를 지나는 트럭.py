from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    done = 0
    w_sum = 0
    sum_truck = sum(truck_weights)
    truck_weights = deque(truck_weights)
    bridge = deque([0 for x in range(bridge_length)])
    while done != sum_truck:
        if len(truck_weights)>0:
            poped = bridge.popleft()
            done+=poped
            w_sum-=poped
            truck = truck_weights.popleft()
            if w_sum+truck<=weight:
                bridge.append(truck)
                w_sum+=truck
            else: 
                bridge.append(0)
                truck_weights.appendleft(truck)
        else:
            poped = bridge.popleft()
            bridge.append(0)
            done+=poped
        answer+=1
    return answer