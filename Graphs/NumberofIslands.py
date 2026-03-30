class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows = len (grid)
        cols = len (grid[0])
        islands = 0

        def dfs (x,y):
            if x < 0 or x >= rows or y <0 or y >= cols or grid [x][y] != "1": # always put the correct condition
                return
            grid [x][y] = "0"
            dfs (x+1, y)
            dfs (x-1, y)
            dfs (x, y+1)
            dfs (x, y-1)
        
        for i in range (rows):
            for j in range (cols):
                if grid [i][j] == "1":
                    islands += 1
                    dfs (i,j)

        return islands
