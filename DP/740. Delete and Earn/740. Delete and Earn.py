from typing import *

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        res=nums[0]
        dp=[]
        nums.sort()
        for i in range(len(nums)):
            tmp=0
            for x in reversed(range(i)):
                if nums[x]!=nums[i]+1 and nums[x]!=nums[i]-1:
                    tmp=max(tmp,dp[x]+nums[i])
            tmp2=max(tmp,nums[i])
            dp.append(tmp2)
            res=max(res,tmp2)
        print(dp)
        return res

call=Solution()
call.deleteAndEarn([1,1,1,2,4,5,5,5,6])