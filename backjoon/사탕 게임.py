n = int(input())

colors = []
for _ in range(n):
    ls = []
    for col in input():
        ls.append(col)
    colors.append(ls)

direction = [[1,0],[0,1]]

def count(maps):
    counts = []
    for i in range(n):
        tmp = maps[i][0]
        count = 1
        for j in range(1, n):
            if tmp == maps[i][j]:
                count += 1
            else:
                tmp = maps[i][j]
                counts.append(count)
                count = 1        
        counts.append(count)           
    for j in range(n):
        tmp = maps[0][j]
        count = 1
        for i in range(1, n):
            if tmp == maps[i][j]:
                count += 1
            else:
                tmp = maps[i][j]
                counts.append(count)
                count = 1     
        counts.append(count)                   
    return max(counts)
answer = 0
cnt = count(colors)
for i in range(n):
    for j in range(n):
        for x, y in direction:
            if 0<=i+x<n and 0<=j+y<n and colors[i][j] != colors[i+x][j+y]:
                a = colors[i][j]
                b = colors[i+x][j+y]
                colors[i][j] = b
                colors[i+x][j+y] = a
                cnt = count(colors)
                if cnt > answer:
                    answer = cnt               
                colors[i][j] = a
                colors[i+x][j+y] = b
print(answer)                