class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i: [] for i in range(n)}
        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)
        
        visited = [False] * n
        
        def bfs(i):
            nonlocal visited
            q = deque([i])
            visited[i] = True
            while q:
                t = q.popleft()
                for neig in adj[t]:
                    if not visited[neig]:
                        visited[neig] = True
                        q.append(neig)
        count = 0
        for i in range(n):
            if not visited[i]:
                bfs(i)
                
                count += 1
        return count 