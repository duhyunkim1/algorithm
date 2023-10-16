def dfs(i, j, moves, length, visited, maps, number, puzzles):
    for dx, dy in moves:
        if 0<=i+dx<length and 0<=j+dy<length and not visited[i+dx][j+dy] and maps[i+dx][j+dy] == number:
            visited[i+dx][j+dy] = True
            puzzles.append([i+dx, j+dy])
            dfs(i+dx, j+dy, moves, length, visited, maps, number, puzzles)
    return visited, puzzles

def find_number(maps, number):
    puzzles_all = []
    moves = [[0,1],[0,-1],[1,0],[-1,0]]
    length = len(maps)
    visited = [[False for _ in range(length)] for _ in range(length)]
    for i in range(length):
        for j in range(length):
            if maps[i][j] == number and not visited[i][j]:
                visited[i][j] = True
                visited, puzzles = dfs(i, j, moves, length, visited, maps, number, [[i, j]])
                puzzles_all.append(puzzles)
    return puzzles_all

def compare(maps, blank, puzzle, answer, solved):
    used = [False for _ in range(len(puzzle))]
    for idx_b in range(len(blank)):
        if solved[idx_b] == True:
            continue
        for idx_p in range(len(puzzle)):
            if used[idx_p]:
               continue 
            if len(blank[idx_b]) != len(puzzle[idx_p]):
                continue
            flag = True
            for i, (b, p) in enumerate(zip(blank[idx_b], puzzle[idx_p])):
                if i == 0:
                    bx_init, by_init = b
                    px_init, py_init = p                                       
                else:
                    if not(b[0]-bx_init == p[0]-px_init and b[1]-by_init == p[1]-py_init):
                        flag = False             
                        break
            
            if flag == True:
                answer+=len(blank[idx_b])
                solved[idx_b] = True
                used[idx_p] = True
                for x, y in puzzle[idx_p]:
                    maps[x][y] = 0
                break
    return maps, answer, solved
  
def lotate_maps(maps):
    length = len(maps)
    new = []
    for j in range(length):
        line = []
        for i in range(length):
            line.append(maps[i][length-j-1])
        new.append(line)
    return new

def solution(game_board, table):
    answer = 0 
    blank = find_number(game_board, 0)
    solved = [False for _ in range(len(blank))]
    for _ in range(4):
        puzzle = find_number(table, 1)
        table, answer, solved = compare(table, blank, puzzle, answer, solved)
        table = lotate_maps(table)
        print(table)
    return answer