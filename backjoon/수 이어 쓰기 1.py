n = input()
length = len(n)
n = int(n)

answer = 0
for i in range(1, length+1):
    if i == length:
        answer += i*(n-10**(i-1)+1)
    else:
        answer += i*9*(10**(i-1))

print(answer)