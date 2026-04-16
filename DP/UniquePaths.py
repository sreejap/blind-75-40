# https://leetcode.com/problems/unique-paths/
class Solution:    
    def uniquePaths(self, m: int, n: int) -> int:
        paths = [[1]*n for _ in range(m)]

        for i in range (1,m):
            for j in range (1,n):
                # the path to i,j is number of paths to i-1,j and number of paths to i,j-1
                paths[i][j] = paths [i-1][j] + paths [i][j-1]
        return paths [m-1][n-1]
