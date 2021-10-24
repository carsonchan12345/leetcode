from typing import *
class Solution:
    def rob(self, nums: List[int]) -> int:
        dp=nums.copy()

        for d in range(1,len(dp)):
            tmpmax=0
            for i in range(0,d-1):
                tmpmax=max(tmpmax,dp[i])
            dp[d]+=tmpmax
        res=0
        print(dp)
        for d in dp:
            res=max(res,d)
        return res
nums = [2,7,9,3,1]
call=Solution()
print(call.rob(nums))


