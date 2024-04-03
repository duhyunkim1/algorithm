n = int(input())
d = {}
for _ in range(n):
    word = input()
    for i, x in enumerate(word):
        try:
            d[x] += 10 ** (len(word)-i-1)
        except:
            d[x] = 10 ** (len(word)-i-1)
d = sorted(d.items(), key = lambda x: x[1], reverse=True)
answer = 0
for i, x in enumerate(range(9, 9-len(d), -1)):
    answer += x*d[i][1]
print(answer)