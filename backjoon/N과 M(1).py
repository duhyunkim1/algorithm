from collections import deque
n, m = map(int, input().split(' '))
numbers = [x for x in range(1, n+1)]

def bfs(queue, m):
    while queue:
        now = queue.popleft()
        if len(now) == m:
            now = map(str, now)
            print(' '.join(now))
            continue
        for number in numbers:
            if number not in now:
                queue.append(now+[number])
                
for number in numbers:
    queue = deque([[number]])
    bfs(queue, m)        