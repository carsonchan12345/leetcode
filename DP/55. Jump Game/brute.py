from typing import *
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        canReach=[False]*len(nums)
        canReach[0]=True
        head=0
        for i in range(len(nums)):
            if canReach[i]==True and i+nums[i]>head:
                for x in range(head,head+nums[i]-(head-i)+1):
                    if x>=len(nums):
                        break
                    canReach[x]=True
                head=i+nums[i]
        print(head)
        print(canReach)
        return canReach[len(nums)-1]
nums = [3,4,0,1,0,0,3,0]
call=Solution()
print(call.canJump(nums))
