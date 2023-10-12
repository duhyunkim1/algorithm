import sys
N = int(input())
corr = [list(map(int, input().split(' '))) for _ in range(N)]
teams = []
def dfs(players, team):
    global teams
    if len(team) == N/2:
        teams.append(team)
    for i, p in enumerate(players):
        dfs(players[i+1:], team+[players[i]])
        
dfs(list(range(N)), [])
result = sys.maxsize

for team in teams:
    score1 = 0
    score2 = 0
    for i in range(N):
        for j in range(N):
            if i in team and j in team:
                score1+=corr[i][j]
            if i not in team and j not in team:
                score2+=corr[i][j]
                
    if result > abs(score1-score2):
        result = abs(score1-score2)

print(result)