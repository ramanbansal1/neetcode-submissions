from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        adj = {}
        m = len(beginWord)

        for word in wordList:
            for i in range(m):
                pattern = word[:i] + "*" + word[i + 1:]
                adj.setdefault(pattern, []).append(word)

        def bfs():
            queue = deque([beginWord])
            visited = {beginWord}
            steps = 1

            while queue:
                for _ in range(len(queue)):
                    word = queue.popleft()

                    if word == endWord:
                        return steps

                    for i in range(m):
                        pattern = word[:i] + "*" + word[i + 1:]

                        for nei in adj.get(pattern, []):
                            if nei not in visited:
                                visited.add(nei)
                                queue.append(nei)

                steps += 1

            return 0

        return bfs()