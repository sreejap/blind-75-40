# https://leetcode.com/problems/word-search/
# Time Complexity: O(m × n × 4^L)

# Where:

# m = number of rows
# n = number of columns
# L = length of the word
# Breakdown:

# m × n: We potentially start DFS from every cell in the grid
# 4^L: From each starting cell, DFS explores up to 4 directions at each step, for L levels deep
# Note: This is the worst-case bound. In practice, it's much faster due to pruning:

# DFS stops immediately when the current character doesn't match
# Most paths are cut off early
# Space Complexity: O(L)

# Where:

# L = length of the word
# Breakdown:

# Recursion stack: Maximum depth is L (the word length)
# In-place marking: The board modification ("#" marking) uses no extra space
# No additional data structures like visited sets are needed
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len (board)
        COLS = len (board[0])

        def dfs (x,y,idx,visited):
            # check bounds and character match before proceeding
            if x < 0 or x >= ROWS or y < 0 or y >= COLS or (x,y) in visited or board[x][y]!=word[idx]:
                return False
            
            # word found when index reaches end
            if idx == len (word)-1:
                return True
            
            # track visited cells to prevent reuse
            visited.add((x,y))

            # explore neighbors in all 4 directions
            res = dfs (x+1,y,idx+1,visited) or dfs (x-1,y,idx+1,visited) or dfs (x,y+1,idx+1,visited) or dfs (x,y-1,idx+1,visited)

            # backtrack
            visited.remove ((x,y))
            return res

        # search starts from every cell in the board
        for r in range(ROWS):
            for c in range(COLS):
                if dfs (r,c,0,set()):
                    return True
        
        return False
