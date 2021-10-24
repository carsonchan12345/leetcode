from typing import *

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res=[]
        curr=[]
        nums.sort()
        def dfs(used:List[bool], target:int):
            level=len(curr)
            print(curr)
            if level==target:   
                res.append(curr.copy())
                return
            if level>target:
                return

            prev=-11
            for i in range(0,len(nums)):
                if used[i] or prev==nums[i]:
                    continue
                else:
                    prev=nums[i]
                    used[i]=True
                    curr.append(nums[i])
                    dfs(used, target)
                    curr.pop()
                    used[i]=False

        dfs([False]*len(nums),len(nums))
        return res

call=Solution()
print(call.permuteUnique([1,2,3]))
