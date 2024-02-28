#permutation 시간 복잡도 N! 다음 순열을 구하는 시간 복잡도 O(N) 모든 순열을 구하는 시간 복잡도 O(N!*N)
#첫 순열은 오름차순, 비 내림차순
#마지막 순열은 내림차순, 비 오름차순
#다음 순열만 구하는 법이 따로 있음. python은 itertools를 활용하면 됨.
#~의 가장 긴 마지막 순열인지를 먼저 찾아야함 예시: A가 7236541이면 A는 723의 마지막 순열
#뒤에서부터 내림창순이 얼마나 진행되는지 알아야함.
def next_permutation(a):
    i = len(a) - 1
    while i > 0 and a[i-1] >= a[i]:
        i -= 1
    if i <= 0:
        return False
    
    j = len(a)-1
    while a[j] <= a[i-1]:
        j -= 1
    
    a[i-1], a[j] = a[j], a[i-1]
    
    j = len(a)-1
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1
    return True

n = int(input())
a = list(map(int, input().split()))
if next_permutation(a):
    print(' '.join(map(str, a)))
else:
    print(-1)