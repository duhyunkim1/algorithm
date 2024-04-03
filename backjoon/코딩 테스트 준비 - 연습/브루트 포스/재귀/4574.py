def setting():
    sudoku = [[0 for _ in range(9)] for _ in range(9)]
    tile = [[0 for _ in range(10)] for _ in range(10)]
    
    n = int(input())      
    if n == 0:
        return 0, 0, 0, 0, 0

    for _ in range(n):
        u, lu, v, lv = input().split()
        sudoku[ord(lu[0])-65][int(lu[1])-1] = int(u)
        sudoku[ord(lv[0])-65][int(lv[1])-1] = int(v)
        
        tile[int(u)][int(v)] = 1
        tile[int(v)][int(u)] = 1
        
    for i, grid in enumerate(list(input().split())):
        sudoku[ord(grid[0])-65][int(grid[1])-1] = i+1
        
    blank = []
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                blank.append([i,j])
                
    num_blank = len(blank)
    return n, sudoku, tile, blank, num_blank

def get_possible(i, j):
    ls = []
    for x in range(i//3*3, i//3*3+3):
        for y in range(j//3*3, j//3*3+3):
            ls.append(sudoku[x][y])
    
    for x in range(9):
        ls.append(sudoku[i][x])
        ls.append(sudoku[x][j])
        
    psb = []
    for x in range(1, 10):
        if x not in ls:
            psb.append(x)        

    return list(set(psb))

def dfs(step):
    global flag
    if step == num_blank-1 and flag == True:
        for sdk in sudoku:
            print(''.join(map(str, sdk)))
        flag = False
        return 
    if flag == False:
        return
    i = blank[step][0]
    j = blank[step][1]
    
    if sudoku[i][j] != 0:
        dfs(step+1)
        return
    
    for dx, dy in direction:
        if 0<=i+dx<9 and 0<=j+dy<9 and sudoku[i+dx][j+dy] == 0:
            possible1 = get_possible(i, j)
            possible2 = get_possible(i+dx, j+dy)
            for a in possible1:
                for b in possible2:

                    if a == b:
                        continue
                    if tile[a][b] == 0:
                        sudoku[i][j] = a
                        sudoku[i+dx][j+dy] = b
                        tile[a][b] = 1
                        tile[b][a] = 1
       
                        dfs(step+1)
                
                        sudoku[i][j] = 0
                        sudoku[i+dx][j+dy] = 0
                        tile[a][b] = 0
                        tile[b][a] = 0
       
                        
direction = [[1,0],[0,1]]
case = 1
while True:
    n, sudoku, tile, blank, num_blank = setting()
    if n == 0:
        break
    print(f'Puzzle {case}')
    flag = True
    dfs(0)
    case+=1
    