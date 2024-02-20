import heapq
N, C = map(int, input().split(' '))
house = [int(input()) for _ in range(N)]
for i in range(N-1):
    house[i]