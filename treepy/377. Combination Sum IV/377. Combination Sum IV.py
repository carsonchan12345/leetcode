from typing import *

class Solution:

    def __init__(self) -> None:
        pass
    def combinationSum4(self, nums: List[int], target: int) -> int:
        res=[]
        self.dfs(nums, target, res, [],0)
        return len(res)
    
    def dfs(self, nums: List[int], target: int, res:list, curr:list, sum:int):

        if sum==target:
            res.append(curr.copy())
            return
        if sum>target:
            return
        
        for i in range(0,len(nums)):
            curr.append(nums[i])
            self.dfs(nums, target, res, curr, sum+nums[i])
            curr.pop()
        
        


call=Solution()
print(call.combinationSum4([4,2,1],32))