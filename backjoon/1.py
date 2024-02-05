while True:
    try:
        case = int(input())
        i = 1 
        while case:
            if int('1'*i) % case == 0:
                print(i)
                break
            else:
                i = i+1
    except:
        break