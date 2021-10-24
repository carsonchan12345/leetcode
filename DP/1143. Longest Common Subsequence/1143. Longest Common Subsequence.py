class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp=[[0 for col in range(len(text1)+1)] for row in range(len(text2)+1)]
        for row in reversed(range(0,len(text2))):
            for col in reversed(range(0,len(text1))):
                if (text1[col]==text2[row]):
                    dp[row][col]=dp[row+1][col+1] + 1
                else:
                    dp[row][col]=max(dp[row+1][col],dp[row][col+1])

        return dp[0][0]
        
text1 = "bsbininm"

text2 = "jmjkbkjkv"
call=Solution()
print(call.longestCommonSubsequence(text1,text2))