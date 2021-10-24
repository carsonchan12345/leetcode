class Solution:
    def climbStairs(self, n: int) -> int:
        
        dp ={new: int() for new in range(n+1)}
        dp[0]=1
        for x in range(1,n+1):
            dp[x]+=dp[x-1]
            if x-2>=0:
                dp[x]+=dp[x-2]
        return dp[n]
                





call=Solution()
print(call.climbStairs(3))