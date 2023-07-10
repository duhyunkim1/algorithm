import math
def solution(progresses, speeds):
    time = []
    for p, s in zip(progresses, speeds):
        time.append(math.ceil((100-p)/s))
    answer = []
    while len(time) != 0:
        dtb = 0
        for t in time:
            if t <= time[0]:
                dtb +=1
            else:
                break
        del time[:dtb]                
        answer.append(dtb)            
    return answer