num = int(input())
flag = True
if num == 1:
    print(1)
    exit()
else:
    num-=1
turn = 0
start = 1
while flag:
    for x in range(start, start+6*turn):
        if x == num:
            print(turn+1)
            flag = False
            break
    start += 6*turn
    turn+=1