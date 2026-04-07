from typing import List

class Solution:
    def containsCycle(self, grid):
        rows, cols = len(grid), len(grid[0])
        visited = [[False] * cols for _ in range(rows)]

        def dfs(r, c, pr, pc):
            if visited[r][c]:
                return True

            visited[r][c] = True
            val = grid[r][c]

            directions = [(1,0), (-1,0), (0,1), (0,-1)]

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == val:
                    # skip the parent cell
                    if nr == pr and nc == pc:
                        continue

                    if dfs(nr, nc, r, c):
                        return True

            return False

        for r in range(rows):
            for c in range(cols):
                if not visited[r][c]:
                    if dfs(r, c, -1, -1):
                        return True

        return False

grid = [["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]]
sol = Solution()
sol.containsCycle(grid)