def get_all_cctv(cctv):
    all = []
    for i in range(4):
        all.append([cctv[j%4] for j in range(i, i+4)])
    return all
    
directions = [[1,0],[0,1],[-1,0],[0,-1]]
    
def check_maps(cam, x, y, space):
    for c, (dx, dy) in zip(cam, directions):
        if c == 1:
            length = 1
            while True:
                if 0 <= x+length*dx < n and 0 <= y+length*dy < m: 
                    tmp = space[x+length*dx][y+length*dy]
                    if tmp != 6:
                        space[x+length*dx][y+length*dy] = 1
                    else: 
                        
                        break
                else:
                    break
                length += 1
    return space

cctv = [[1,0,0,0], [1,0,1,0], [1,1,0,0], [1,1,1,0], [1,1,1,1]]
cctv_all = {}
for i, c in enumerate(cctv):
    cctv_all[i+1] = get_all_cctv(c)

n, m = map(int, input().split(' '))
space = [list(map(int, input().split(' '))) for _ in range(n)]

obj = []
for i in range(n):
    for j in range(m):
        if space[i][j] != 0 and space[i][j] != 6:
            obj.append([space[i][j], i, j])
            space[i][j] =1
answer = []

def dfs(now, space):
    global answer
    if now == len(obj):
        sum_v = 0
        for x in space:
            sum_v += x.count(0)
        answer.append(sum_v)
        
        return
    space_copy = [[j for j in space[i]] for i in range(n)]
    cam, x, y = obj[now]
    for c in cctv_all[cam]:
        space = check_maps(c, x, y, space)
        dfs(now+1, space)
        space = [[j for j in space_copy[i]] for i in range(n)]
dfs(0, space)

print(min(answer))