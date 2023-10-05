
# https://leetcode.com/problems/minimum-path-sum/submissions/


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        dp = [[0 for i in range(n)] for j in range(m)]
        
        dp[0][0] = grid[0][0]
        for i in range(1,m):
            dp[i][0] = grid[i][0] + dp[i-1][0]
            
        for j in range(1,n):
            dp[0][j] = grid[0][j] + dp[0][j-1]
            
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = grid[i][j] + min(dp[i][j-1],dp[i-1][j])
                
        return dp[-1][-1]