a, b, c = map(int, input().split(' '))
answer = 1
while True:
    x = answer//15
    y = answer//28
    z = answer//19
    if 15*x+a == 28*y+b == 19*z+c:
        print(15*x+a)
        break
    answer += 1