sudoku = [list(map(int, input().split())) for _ in range(9)]
                
def get_set(i, j):
    ls = []
    for x in range(i//3*3, i//3*3+3):
        for y in range(j//3*3, j//3*3+3):
            ls.append(sudoku[x][y])
    
    for x in range(9):
        ls.append(sudoku[x][j])
        ls.append(sudoku[i][x])
    
    return list(set(ls))
            
def dfs(step):
    if step == n:
        for sdk in sudoku:
            print(' '.join(map(str, sdk)))                
        exit()        
    
    i = blank[step][0]
    j = blank[step][1]

    include = get_set(i, j)
    
    for num in range(1, 10):
        if num not in include:
            sudoku[i][j] = num
            dfs(step+1)
            sudoku[i][j] = 0
        
blank = []
for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            blank.append([i, j])
n = len(blank)        
dfs(0)