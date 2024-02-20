N = int(input())
inputs = list(map(int, input().split(' ')))

for input in inputs:
    if input == 1:
        N -= 1
    else:
        for i in range(2, input):
            if i*i <= input and input%i == 0:
                N -= 1
                break
print(N)            