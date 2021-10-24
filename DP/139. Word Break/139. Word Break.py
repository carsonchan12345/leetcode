from typing import *
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp={x: False for x in range(len(s)+1)}
        dp[len(s)+1]=True

        for i in reversed(range(0,len(s))):
            for w in wordDict:
                if i+len(w)<len(s) and s[i:i+len(w)]==w:
                    dp[i]=dp[i+len(w)]
                    if dp[i]:
                        break
        return dp[0]



        
s = "aaaaaaa"
wordDict = ["aaaa","aaa"]
call=Solution()
print(call.wordBreak(s,wordDict))

