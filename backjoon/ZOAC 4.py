H, W, N, M = map(int, input().split(' '))
def get_number(length, space):        
    next_sit = 0
    num = 0
    for l in range(length):
        if l == next_sit:   
            num += 1 
            next_sit += (space+1)
    return num
print(get_number(H, N) * get_number(W,M))