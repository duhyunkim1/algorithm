from collections import deque
def solution(begin, target, words):
    visited = [0 for _ in range(len(words))]
    begin = [x for x in begin]
    target = [x for x in target]
    words = [[x for x in word] for word in words] 
    queue = deque([begin])
    while queue:
        start = queue.popleft()
        if start == target:
            return visited[words.index(target)] 
        for idx, word in enumerate(words):
            count = 0
            for x, y in zip(word, start):
                if x != y:
                    count += 1
            if count == 1 and visited[idx] == 0:
                if begin == start:
                    visited[idx] = 1
                else:
                    visited[idx] = visited[words.index(start)]+1
                queue.append(word)
    return 0
