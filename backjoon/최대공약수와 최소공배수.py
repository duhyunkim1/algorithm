import sys
num1, num2 = map(int, sys.stdin.readline().split(' '))

for n in range(num1, 0, -1):
    if num1%n == 0 and num2%n == 0:
        print(n)
        break
i = 1
while True: 
    if num1*i % num2 == 0:
        print(num1*i)
        break
    i += 1