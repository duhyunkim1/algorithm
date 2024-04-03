case = 1
while True:
    a = list(map(int, input().split()))
    k = a[0]
    if k == 0:
        break
    else:
        if case > 1:
            print()
        case +=1
    s = a[1:]
    answers = []
    
    def dfs(k, s, now, lotto):
        global answers
        if k == 0:
            if lotto:
                print(' '.join(map(str, now)))
            else:
                answers.append(now)
            return
            

        for idx, num in enumerate(s):
            if num not in now:
                dfs(k-1, s[idx+1:], now+[num], lotto)
    
    dfs(k, s, [], False)
    for ls in answers:
        dfs(6, ls, [], True)