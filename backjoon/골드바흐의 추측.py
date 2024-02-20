import sys
input = sys.stdin.readline

MAX = 1000000
check = [0] * (MAX+1)
check[0] = check[1] = True
prime = []
for i in range(2, int(MAX**0.5)+1):
    if check[i] == False:
        prime.append(i)
        for j in range(i+i, MAX, i):
            check[j] = True
prime = prime[1:]

while True:
    num = int(input())
    if num == 0:
        break
    for p in prime:
        if check[num-p] == False:
            print('{0} = {1} + {2}'.format(num, p, num-p))
            break