N, M = map(int, input().split(' '))
maps = [list(map(int, input().split(' '))) for _ in range(N)]
def type1(x,y):
    case1 = [[x, y+1],[x, y+2],[x, y+3]]
    case2 = [[x+1, y],[x+2, y],[x+3, y]]
    return [case1, case2]

def type2(x,y):
    case1 = [[x+1,y], [x,y+1],[x+1,y+1]]
    return [case1]

def type3(x,y):
    case1 = [[x+1, y], [x+2,y ], [x+2,y+1]]
    case2 = [[x, y-1], [x,y-2], [x+1, y-2]]
    case3 = [[x-1, y], [x-2, y], [x-2, y-1]]
    case4 = [[x, y+1], [x, y+2], [x-1, y+2]]
    
    case5 = [[x+1, y], [x+2, y], [x+2, y-1]]
    case6 = [[x, y-1], [x, y-2], [x-1, y-2]]
    case7 = [[x-1, y], [x-2, y], [x-2, y+1]]
    case8 = [[x, y+1], [x, y+2], [x+1, y+2]]
    return [case1, case2, case3, case4, case5, case6, case7, case8]

def type4(x,y):
    case1 = [[x+1, y], [x+1, y+1], [x+2, y+1]]
    case2 = [[x, y-1], [x+1, y-1], [x+1, y-2]]
    case3 = [[x-1, y], [x-1, y-1], [x-2, y-1]]
    case4 = [[x, y+1], [x-1, y+1], [x-1, y+2]]
    
    case5 = [[x+1, y], [x+1, y-1], [x+2, y-1]]
    case6 = [[x, y-1], [x-1, y-1], [x-1, y-2]]
    case7 = [[x-1, y], [x-1, y+1], [x-2, y+1]]
    case8 = [[x, y+1], [x+1, y+1], [x+1, y+2]]
    return [case1, case2, case3, case4, case5, case6, case7, case8]

def type5(x, y):
    case1 = [[x, y+1],[x, y+2],[x+1, y+1]]
    case2 = [[x+1, y],[x+2, y],[x+1, y-1]]
    case3 = [[x, y-1],[x, y-2],[x-1, y-1]]
    case4 = [[x-1, y],[x-2, y],[x-1, y+1]]
    return [case1, case2, case3, case4]

answer = 0
for i in range(N):
    for j in range(M):
        cases = []
        cases.extend(type1(i,j))
        cases.extend(type2(i,j))
        cases.extend(type3(i,j))
        cases.extend(type4(i,j))
        cases.extend(type5(i,j))
        
        for case in cases:
            tmp = maps[i][j]
            flag = 0
            for x, y in case:
                if 0<=x<N and 0<=y<M:
                    tmp += maps[x][y]
                else:
                    flag = 1
                    break
            if flag == 0 and tmp > answer:
                answer = tmp
print(answer)
                
                