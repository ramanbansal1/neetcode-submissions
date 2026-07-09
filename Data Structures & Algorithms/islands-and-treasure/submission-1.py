from collections import deque
from typing import List

INF = 2147483647

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> List[List[int]]:
        rows, cols = len(grid), len(grid[0])
        queue = deque()

        # Add all treasure cells to the queue
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r, c))

        directions = [
            (1, 0),   # Down
            (-1, 0),  # Up
            (0, 1),   # Right
            (0, -1),  # Left
        ]

        while queue:
            r, c = queue.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                # Skip cells outside the grid
                if not (0 <= nr < rows and 0 <= nc < cols):
                    continue

                # Only visit unprocessed land cells
                if grid[nr][nc] == INF:
                    grid[nr][nc] = grid[r][c] + 1
                    queue.append((nr, nc))


