from typing import *
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res=0
        dp={x: int(1) for x in range(len(nums))}

        for n in reversed(range(len(nums))):
            tmp=1
            for check in range(n+1,len(nums)):
                if nums[n]<nums[check]:
                    tmp=max(tmp,dp[check]+1)
            dp[n]=tmp

        for n in range(len(nums)):
            res=max(res,dp[n])
        
        return res
nums = [7,7,7,7,7,7,7]
call= Solution()
print(call.lengthOfLIS(nums))



            
