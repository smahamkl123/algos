from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        totIslands = 0

        
        def dfs(row: int, col: int):
            if col < 0 or col >= len(grid[0]) or row < 0 or row >= len(grid) or grid[row][col] == '0':
                return
            
            # already visited cells set to 0
            grid[row][col] = '0'

            dfs(row+1, col)
            dfs(row-1, col)
            dfs(row, col+1)
            dfs(row, col-1)
        
        # iterate through the grid and once it encounters a land (1) start the DFS search
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    totIslands += 1
                    dfs(row, col)

        return totIslands