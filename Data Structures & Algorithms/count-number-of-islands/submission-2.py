class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1,0],[0,-1],[0,1],[-1,0]]
        islands = 0
        row = len(grid)
        col = len(grid[0])
        def dfs(x,y):
            if x < 0 or y < 0 or x >= row or y >= col or grid[x][y] == "0":
                return
            grid[x][y] = "0"
            for dr, dc in directions:
                dfs(x + dr, y + dc)
        
        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1":
                    dfs(r, c)
                    islands += 1
        return islands
        


            