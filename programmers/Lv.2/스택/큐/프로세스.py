def solution(priorities, location):
    answer=0
    init_location = list(range(len(priorities)))
    fix_prior = sorted(priorities)
    while True:
        lct = init_location.pop(0)
        prior = priorities.pop(0)
        if fix_prior[-1] != prior: 
            init_location.append(lct)
            priorities.append(prior)
        else:
            fix_prior.pop()
            answer+=1
            if lct == location:
                return answer