from collections import deque

def distance(start, end):
    return abs(start[0]-end[0])+abs(start[1]-end[1])

def bfs(i, j):
    queue = deque([[i, j]])
    while queue:
        i, j = queue.popleft()
        if distance([i, j], [festival_x, festival_y]) <= 1000:
            return "happy"
        for n, store in enumerate(stores):
            if distance([i, j], store) <= 1000 and not visited[n]:
                queue.append(store)
                visited[n] = True
    return "sad"
t = int(input())
for _ in range(t):
    num_store = int(input())
    house_x, house_y = map(int, input().split(' '))
    stores = []
    for _ in range(num_store):
        store_x, store_y = map(int, input().split(' '))
        stores.append([store_x, store_y])
    festival_x, festival_y = map(int, input().split(' '))
    
    visited = [False for _ in range(num_store+1)]
    result = bfs(house_x, house_y)
    print(result)