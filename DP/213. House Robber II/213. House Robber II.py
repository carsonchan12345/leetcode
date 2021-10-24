from typing import *
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        dp1=nums.copy()
        dp2=nums.copy()
        dp1.pop()
        dp2.pop(0)
        res=0
        
        for d in range(1,len(dp1)):
            tmpmax=0
            for i in range(0,d-1):
                tmpmax=max(tmpmax,dp1[i])
            dp1[d]+=tmpmax
        print(dp1)

        for d in range(1,len(dp2)):
            tmpmax=0
            for i in range(0,d-1):
                tmpmax=max(tmpmax,dp2[i])
            dp2[d]+=tmpmax
        print(dp2)


        for d in dp1:
            res=max(res,d)
        for d in dp2:
            res=max(res,d)
        return res
nums = [1,2,3]
call=Solution()
print(call.rob(nums))


