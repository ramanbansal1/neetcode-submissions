class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {i:[] for i in range(n)}
        for i,j in edges:
            adj[i].append(j)
            adj[j].append(i)


        visited = set()
        def dfs(path):

            i = path[-1]
            if i in visited:
                return True
            else:
                visited.add(i)
            
            for j in adj[i]:
                if len(path) >= 2 and j == path[-2]:
                    continue
                if j in path:
                    return False

                if not dfs(path+[j]):
                    return False
            return True
        
    
        if not dfs([0]):
            return False
        return len(visited) == n
            