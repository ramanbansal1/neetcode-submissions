class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = [[] for _ in range(n + 1)]

        def dfs(node, par):


            if visit[node] == True:
                return True
            
            visit[node] = True

            for nei in adj[node]:
                if nei == par:
                    continue
                if dfs(nei, node):
                    return True
            return False





        for i, j in edges:
            adj[i].append(j) 
            adj[j].append(i) 
            visit = [False] * (n + 1)

            if dfs(i, -1):
                return [i, j]
        
        return []