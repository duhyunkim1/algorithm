dp = [0 for _ in range(1001)]
n = int(input())
cards = [0]
cards+= list(map(int, input().split(' ')))

for i in range(2, n+1):
    for k in range(i):
        cards[i] = min([cards[i], cards[i-k]+cards[k]])
print(cards[-1])
