def solution(s):
    answer = True
    left = []
    for x in s:
        if x == '(':
            left.append(0)
        else:
            try:
                left.pop()
            except:
                return False
    if len(left) == 0:
        return True
    else:
        return False