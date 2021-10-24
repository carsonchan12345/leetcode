class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp=[[0]*n]*m
        print(dp)
        dp[m-1][n-1]=1

        for row in reversed(range(m)):
            for col in reversed(range(n)):
                if row==m-1 or col==n-1:
                    dp[row][col]=1
                else:
                    dp[row][col]=dp[row+1][col]+dp[row][col+1]

        print(dp)
        return dp[0][0]

call=Solution()
print(call.uniquePaths(3,3))