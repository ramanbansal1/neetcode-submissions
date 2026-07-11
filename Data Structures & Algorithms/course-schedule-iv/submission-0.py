from collections import deque
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = {i: [] for i in range(numCourses)}
        reachable = [[False] * numCourses for _ in range(numCourses)]
        for i, j in prerequisites:
            adj[i].append(j)
        
        

        for i in adj:
            qu = deque([i])
            visited = [False] * numCourses
            while qu:
                j = qu.popleft()
                if visited[j]:
                    continue
                visited[j] = True

                for neig in adj[j]:
                    qu.append(neig)
                    reachable[i][neig] = True
        result = []
        for ui, uj in queries:
            result.append(reachable[ui][uj])
        
        return result