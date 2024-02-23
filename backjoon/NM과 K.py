n, m, k = map(int, input().split(' '))
maps = [list(map(int, input().split(' '))) for _ in range(n)]

locations = []
for i in range(n):
    for j in range(m):
        locations.append([i, j])
        
def dfs(ls, comb, locations):
    if len(ls) == k:
        comb.append(ls)
    else:
        for idx, loc in enumerate(locations):
            if check(loc[0], loc[1], ls):                
                comb = dfs(ls + [loc], comb, locations[idx+1:])
    return comb            

def check(x, y, ls):
    directions = [[0,0], [-1,0], [0,-1]]
        
    for dx, dy in directions:
        if [x+dx, y+dy] in ls:
            return False
    return True

combinations = dfs([], [], locations)
answer = -10000*k
for comb in combinations:
    tmp = 0
    for x, y in comb:
        tmp += maps[x][y]
    if answer < tmp:
        answer = tmp
print(answer)
        