def solution(queue1, queue2):
    answer = 0
    length = len(queue1)
    half_value = (sum(queue1)+sum(queue2))/2

    start, end = [0, length]
    queue = (queue1 + queue2)*2
    sum_value = sum(queue1) 
    for _ in range(length*4):
        if sum_value == half_value:   
            return answer
            break
        if sum_value > half_value:
            sum_value -= queue[start]
            start += 1
            answer += 1
        else:
            sum_value += queue[end]
            end += 1
            answer += 1   
    answer = -1
    return answer