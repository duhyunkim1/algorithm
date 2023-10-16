N  = int(input())
tiles = [list(map(int, input().split(' '))) for _ in range(N)]

blue = [[0 for _ in range(6)] for _ in range(4)]
green = [[0 for _ in range(4)] for _ in range(6)]

answer = 0
tmp_blue = []
tmp_green = []
def find_location_blue(x, y):
    move = 0
    while y+1 < 6:
        if blue[x][y+1] == 0:
            y += 1
            move += 1
        else:
            break
    return x, y, move

def find_location_green(x, y):
    move = 0
    while x+1 < 6:
        if green[x+1][y] == 0:
            x += 1
            move += 1
        else:
            break
    return x, y, move

for t, x, y in tiles:
    if t == 1: # x y
        i, j, m = find_location_blue(x, 0)
        blue[i][j] = 1
        i, j, m = find_location_green(0, y)
        green[i][j] = 1
    if t == 2: # x y, x y+1
        i, j, m = find_location_blue(x, 0)
        blue[i][j] = 1
        if j-1 >= 0:
            blue[i][j-1] = 1
        else:
            tmp_blue.append([i,j])
        i1, j1, m1 = find_location_green(0, y)
        i2, j2, m2 = find_location_green(0, y+1)
        if m1 == min([m1, m2]):
            green[i1][j1] = 1
            green[i1][j1+1] = 1
        else:
            green[i2][j2] = 1
            green[i2][j2-1] = 1
    if t == 3: # x y, x+1 y
        i1, j1, m1 = find_location_blue(x, 0)
        i2, j2, m2 = find_location_blue(x+1, 0)
        if m1 == min([m1, m2]):
            blue[i1][j1] = 1
            blue[i1+1][j1] = 1
        else:
            blue[i2][j2] = 1
            blue[i2-1][j2] = 1
         
        i, j, m = find_location_green(0, y)
        green[i][j] = 1
        green[i-1][j] = 1
    
    ### check line   
    j = 5
    while j>=0:
        count = 0
        for i in range(4):
            if blue[i][j] == 1:
                count+=1
        if count == 4:
            answer += 1
            for i in range(4):
                blue[i][j] = 0
            for r in range(4):
                for c in range(j-1, -1, -1):
                    blue[r][c+1] = blue[r][c]
                    blue[r][c] = 0
        else:
            j-=1

    i = 5
    while i >= 0:
        count = 0
        for j in range(4):
            if green[i][j] == 1:
                count+=1
        if count == 4:
            answer += 1
            for j in range(4):
                green[i][j] = 0
            for r in range(i-1, -1, -1):
                for c in range(4):
                    green[r+1][c] = green[r][c]
                    green[r][c] = 0    
        else:
            i-=1                                
    count = 0
    for j in range(2):
        for i in range(4):
            if blue[i][j] == 1:
                count+=1
                break
    new_line = [[0 for _ in range(count)] for _ in range(6)]
    for idx, (l, b) in enumerate(zip(new_line, blue)):
        blue[idx] = l + b[:6-count]

    count = 0
    for i in range(2):
        for j in range(4):
            if green[i][j] == 1:
                count+=1
                break
    green = green[0:6-count]
    green = [[0,0,0,0] for _ in range(count)] + green    
    for x, y in tmp_blue:
        blue[x][y] = 1
    for x, y in tmp_green:
        green[x][y] =1
print(answer)

tile = 0 
for i in range(4):
    for j in range(6):
        if blue[i][j] == 1:
            tile +=1
for i in range(6):
    for j in range(4):
        if green[i][j] == 1:
            tile += 1

print(tile)