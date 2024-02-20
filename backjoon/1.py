while True:
    try:
        n = int(input())
        i = 1
        num = 0 
        while True:
            num = num*10+1
            num %= n
            if num == 0:
                print(i)
                break    
            i = i+1        
    except:
        break