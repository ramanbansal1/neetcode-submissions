class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()

        # Add all treasure cells to the queue
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
        queue.append(None)

        directions = [
            (1, 0),   # Down
            (-1, 0),  # Up
            (0, 1),   # Right
            (0, -1),  # Left
        ]
        time = 0

        while queue:
            t = queue.popleft()
            if t == None:
                if not queue:
                    for r in range(rows):
                        for c in range(cols):
                            if grid[r][c] == 1:
                                return -1
                    return time
                time += 1
                queue.append(None)
                continue

            r, c = t


                
            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                # Skip cells outside the grid
                if not (0 <= nr < rows and 0 <= nc < cols):
                    continue

                # Only visit unprocessed land cells
                if grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    queue.append((nr, nc))




