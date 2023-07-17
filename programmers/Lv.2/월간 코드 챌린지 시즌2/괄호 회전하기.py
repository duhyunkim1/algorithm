def solution(s):
    answer = 0
    s = [x for x in s]
    len_s = len(s)
    for i in range(len_s):
        bracket = []
        left = []
        for j in range(len_s): 
            if i+j > len_s-1:
                idx = i+j-len_s
            else:
                idx = i+j       
                
            if s[idx] == '(':
                bracket.append(1)
                left.append(1)
            elif s[idx] == '[':
                bracket.append(2)
                left.append(2)
            elif s[idx] == '{':
                bracket.append(3)  
                left.append(3)
            else:
                if len(left) == 0:
                    bracket = False
                    break
                if s[idx] == ')' and left[-1] == 1:
                    bracket.append(-1)
                    left.pop()
                elif s[idx] == ']' and left[-1] == 2:
                    bracket.append(-2)
                    left.pop()
                elif s[idx] == '}' and left[-1] == 3:
                    bracket.append(-3)
                    left.pop()
        if bracket!=False and sum(bracket) == 0:
            answer+=1
    return answer