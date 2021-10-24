from typing import *
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount==0:
            return 0
        coins.sort()
        dp={new: int(0) for new in range(amount+1)}
        dp[0]=0
        for x in range(1,amount+1):
            tmp=0
            for c in coins:
                if x==c:
                    dp[x]=1
                    tmp=0
                    break
                if x-c>0 and dp[x-c]!=0:
                    if tmp==0:
                        tmp=dp[x-c]
                    else:
                        tmp=min(tmp,dp[x-c])
            if (tmp!=0):
               dp[x]=tmp+1
        print(dp)
        if dp[amount]==0:
            return -1
        else:
            return dp[amount]

coins = [1,2,5]
amount = 11
call=Solution()
print(call.coinChange(coins,amount))