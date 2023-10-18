N = int(input())
maps = [input() for _ in range(N)]
head = False
heart = False
left = None
right = None
left_arm = 0
right_arm = 0
middle = 0
left_leg = 0
right_leg = 0
for i in range(N):
    for j in range(N):
        if maps[i][j] != '*':
            continue
        
        if not head:
            head = [i, j]
            continue
        if i == head[0]+1:
            if j == head[1] and not heart:
                    heart = [i, j]
            elif not heart:
                 left_arm += 1
            elif heart:
                 right_arm += 1
        
        else:
            if j == head[1]:
                middle += 1
                body_end = [i, j]
            else:
                if i == body_end[0] + 1 and left == None:
                    left_leg += 1
                    left = [i, j]
                elif i == body_end[0] + 1 and left != None:
                    right_leg += 1
                    right = [i, j]
                elif left != None and right != None:
                    if j == left[1]:
                        left_leg += 1
                    elif j == right[1]:
                        right_leg += 1
print(heart[0]+1, heart[1]+1)
print(left_arm, right_arm, middle, left_leg, right_leg) 