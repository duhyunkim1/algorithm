from collections import deque
def solution(prices):
    answer = []        
    prices = deque(prices)
    while len(prices) != 0:
        start = prices[0]
        prices.popleft()
        for i, p in enumerate(prices):
            if p < start:
                answer.append(i+1) 
                break
            if i == len(prices)-1:
                answer.append(i+1)
    answer.append(0)
    return answer