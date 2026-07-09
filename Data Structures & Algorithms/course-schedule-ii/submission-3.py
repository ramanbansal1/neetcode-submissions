from collections import deque 
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i : [] for i in range(numCourses)}
        indegree = [0] * numCourses
        for (c, r) in prerequisites:
            adj[r].append(c)
            indegree[c] += 1 

        
        ans = []
        assessed = set({})

        def dfs(node):
            if node in assessed:
                return
            assessed.add(node)
            ans.append(node)


            for nxt in adj[node]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    dfs(nxt)
        
        for i in range(numCourses):
            if indegree[i] == 0:
                dfs(i)
        print(ans)
        return ans if len(ans) == numCourses else []