def solution(brown, yellow):
    total = brown+yellow
    for x in range(2,int(total/2+1)):
        if total%x == 0:
            w = total/x
            h = total/w
            if 2*h+2*(w-2)==brown:
                answer = [w, h]
                break
    return answer