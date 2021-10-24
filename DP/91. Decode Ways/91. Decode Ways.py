class Solution:
    def numDecodings(self, s: str) -> int:
        dp={x: 0 for x in range(len(s))}
        dp[-1]=1
        for i in range(len(s)):
            if s[i]!="0":
                dp[i]=dp[i-1]
            if (i-1>=0 and (s[i-1]=="1" or s[i-1]=="2" and s[i] in "0123456")):
                dp[i]+=dp[i-2]
        print(dp)
        return dp[len(s)-1]

s = "0"
call=Solution()
print(call.numDecodings(s))
