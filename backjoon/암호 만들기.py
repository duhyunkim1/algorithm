l, c = map(int, input().split(' '))
alphabet = list(input().split(' '))
alphabet.sort()

case = ['a', 'e', 'i', 'o', 'u']

def dfs(ls, alphabet, l, case1, case2):
    if len(ls) == l:
        if case1 >= 1 and case2 >= 2:
            print(''.join(map(str, ls)))
        else:
            pass
        return
    for idx, x in enumerate(alphabet):
        if x not in ls:
            if x in case:
                a = 1
                b = 0
            else:
                a = 0
                b = 1
            dfs(ls+[x], alphabet[idx+1:], l, case1+a, case2+b)
dfs([], alphabet, l, 0, 0)