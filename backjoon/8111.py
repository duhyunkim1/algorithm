from collections import deque
def bfs(num):
    queue = deque([(1, '1')])  # (1%num, '1')
    visited = [False] * (num+1)
    visited[1] = True
    i=0
    # 모듈러 연산    
    while queue:
        cur_num, str = queue.popleft()
        # print(i)
        i+=1
        if cur_num == 0:
            return str
        
        if len(str) > 100:
            return 'BRAK'
        
        if not visited[(cur_num*10) % num]:
            visited[(cur_num*10) % num] = True
            queue.append(((cur_num*10)%num, str+'0'))
        
        if not visited[(cur_num*10+1) % num]:
            visited[(cur_num*10+1) % num] = True
            queue.append(((cur_num*10+1)%num, str+'1'))
    
    return 'BRAK'

n = int(input())
for _ in range(n):
    print(bfs(int(input())))