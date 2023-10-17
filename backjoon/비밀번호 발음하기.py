while True:
    word = input()
    if word == 'end':
        break
    condition1 = False
    c2 = True
    condition2 = []
    condition3 = True
    before = ''
    for i, w in enumerate(word):
        if i == 0:
            before = w
        if w in ['a', 'e', 'i', 'o', 'u']:
            condition1 = True
            condition2.append(0)
        else:
            condition2.append(1)
        
        if len(condition2)>=3:
            if condition2[-1] == condition2[-2] == condition2[-3]:
                c2 = False
                break
        if before!='' and w not in ['e', 'o'] and i != 0:
            if w == before:
                condition3 = False
                break
        before = w
    
    if condition1 and c2 and condition3:
        print(f"<{word}> is acceptable.")
    else:
        print(f"<{word}> is not acceptable.")