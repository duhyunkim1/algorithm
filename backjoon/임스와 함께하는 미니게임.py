N, game = input().split(' ')
N = int(N)
if game == 'Y':
    num_p = 1
elif game == 'F':
    num_p = 2
else:
    num_p = 3

names = set()
n_gamer = 0
answer = 0
for _ in range(N):
    name = input()
    if name not in names:
        names.add(name)
        n_gamer += 1
    if n_gamer == num_p:
        answer += 1
        n_gamer = 0
print(answer)