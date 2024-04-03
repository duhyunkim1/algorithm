n, m = map(int, input().split(' '))
space = [list(map(int, input().split())) for _ in range(n)]

directions = [[-1, 0], [0, -1], [-1, -1]]
for i in range(n):
    for j in range(m):
        max = 0
        for dx, dy in directions:
            if 0<=i+dx<n and 0<=j+dy<m:
                if max < space[i+dx][j+dy]:
                    max = space[i+dx][j+dy]
        space[i][j] += max
print(space[-1][-1])