class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        visited = set()

        def dfs(i, j):
            nonlocal perimeter

            visited.add((i, j))

            directions = [
                (-1, 0),
                (1, 0),
                (0, -1),
                (0, 1)
            ]

            for dx, dy in directions:
                nx, ny = i + dx, j + dy

                if not (0 <= nx < len(grid) and 0 <= ny < len(grid[0])):
                    perimeter += 1
                elif grid[nx][ny] == 0:
                    perimeter += 1
                elif (nx, ny) not in visited:
                    dfs(nx, ny)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    dfs(i, j)
                    return perimeter