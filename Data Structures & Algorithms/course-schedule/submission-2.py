class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {}
        for i in range(numCourses):
            adj[i]  = []
        for (c, r) in prerequisites:
            adj[r].append(c)


        def dfs(path):
            elems = adj[path[-1]]

            for i in elems:
                if i in path:
                    return False
                path.append(i)
                if dfs(path): path.pop()
                else: return False
            return True 

        
        for i in range(numCourses):
            if not dfs([i]):
                return False

        return True