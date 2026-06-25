from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])

        queue = deque()
        visited = set()

        # Add all boundary O's
        for i in range(rows):
            for j in range(cols):
                if (i == 0 or j == 0 or i == rows - 1 or j == cols - 1) and board[i][j] == "O":
                    board[i][j] = "#"
                    queue.append((i, j))
                    visited.add((i, j))

        directions = [
            (0, -1),
            (0, 1),
            (1, 0),
            (-1, 0),
        ]

        while queue:
            r, c = queue.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols:
                    if board[nr][nc] == "O" and (nr, nc) not in visited:
                        board[nr][nc] = "#"
                        queue.append((nr, nc))
                        visited.add((nr, nc))

        # Flip enclosed regions
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "#":
                    board[i][j] = "O"