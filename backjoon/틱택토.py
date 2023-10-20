while True:
    case = input()
    if case == 'end':
        break
    games = [[x for x in case[:3]], [x for x in case[3:6]], [x for x in case[6:]]]
    moves = [[1,0],[-1,0],[0,1],[0,-1],[1,1],[-1,1],[1,-1],[-1,-1]]

    x = 0
    o = 0

    win = set()
    for i in range(3):
        for j in range(3):
            if games[i][j] == 'X':
                x+=1
            if games[i][j] == 'O':
                o+=1
            if games[i][j] != '.':
                for dx, dy in moves:
                    if 0 <= i+2*dx < 3 and 0 <= j+2*dy <3 and 0 <= i+dx < 3 and 0 <= j+dy<3:
                        if games[i][j] == games[i+dx][j+dy] and games[i+dx][j+dy] == games[i+2*dx][j+2*dy]:
                            win.update(games[i][j])
                                
    if len(win) > 1:
        print('invalid')    
           
    if len(win) == 1:
        win = list(win)
        if win[0] == 'X' and x == o+1:
            print('valid')
        elif win[0] == 'O' and x == o:
            print('valid')
        else:
            print('invalid')
            
    if len(win) == 0:
        if x+o == 9 and x == o+1:
            print('valid')
        else:
            print('invalid')
