questions = []
while True: 
    line = input()
    if '.' == line:
        break
    else:
        questions.append(line)

for question in questions:
    bracket = []
    flag = 0
    for x in question: 
        if x == "(":
            bracket.append(0)
        if x == "[":
            bracket.append(1)
        if x == ")":
            if len(bracket) == 0:
                print("no")
                flag = 1
                break                    
            if bracket[-1] == 0:
                bracket.pop()
            else:
                print("no")
                flag = 1
                break
        if x == "]":
            if len(bracket) == 0:
                print("no")
                flag = 1
                break
            if bracket[-1] == 1:
                bracket.pop()
            else:
                print("no")
                flag = 1
                break
    if flag == 0:                
        if len(bracket)==0:
            print("yes")
        else:
            print("no")
