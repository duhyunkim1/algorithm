import heapq
N = int(input())
oils = [list(map(int, input().split(' '))) for _ in range(N)]
oils.sort(key=lambda x: x[0])
L, P = map(int, input().split(' '))

queue = []
heapq.heappush(queue, [P, 0, 0])
for i in range(N+1):
    sk, P, answer = heapq.heappop(queue)
    if L - sk - P <= 0 :        
        print(answer)
        exit()
    candidate = sk
    next = False
    for length, fill in oils:
        if P >= (length-sk) and sk < length:
            if candidate < length + P+(fill - (length - sk)):
                next = [ P+(fill - (length - sk)), length, answer+1]
                heapq.heappush(queue, next)
            
print(-1)        
        
        
# 5
# 1 5
# 5 7
# 6 1
# 7 10
# 8 3
# 20 10        