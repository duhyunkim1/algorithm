def searching(i, num_network, computers, visited):
    for j, link in enumerate(computers[i]):
        if link == 1 and visited[j] == False:
            visited[j] = True
            if i == j:
                continue    
            searching(j, num_network, computers, visited)

def solution(n, computers):
    num_network=0
    visited = [False for _ in range(n)]
    for i in range(n):
        if visited[i] != True:
            searching(i, num_network, computers, visited)
            num_network+=1
    return num_network