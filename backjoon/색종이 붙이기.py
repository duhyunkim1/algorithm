import sys 
def dfs(r, c, cnt):
    global ans
    if c >= 10:
        ans = min(ans, cnt)
        return
    if r >= 10:
        dfs(0, c+1, cnt)
        return
    if maps[r][c] == 1:
        for k in range(5):
            if paper[k] >= 5:
                continue
            if r+k >= 10 or c+k >= 10:
                continue
            
            flag = 0
            for tmp_r in range(r, r+k+1):
                for tmp_c in range(c, c+k+1):
                    if maps[tmp_r][tmp_c] == 0:
                        flag = 1
                        break
                if flag == 1:
                    break

            if flag == 0:
                for tmp_r in range(r, r+k+1):
                    for tmp_c in range(c, c+k+1):
                        maps[tmp_r][tmp_c] = 0 
                paper[k] += 1
                dfs(r+k+1, c, cnt+1)
                paper[k] -= 1

                for tmp_r in range(r, r+k+1):
                    for tmp_c in range(c, c+k+1):
                        maps[tmp_r][tmp_c] = 1          
    else: 
        dfs(r+1, c, cnt)


maps = [list(map(int, input().split(' '))) for _ in range(10)]
paper = [0 for _ in range(5)]
ans = sys.maxsize
dfs(0,0,0)
print(ans) if ans != sys.maxsize else print(-1)