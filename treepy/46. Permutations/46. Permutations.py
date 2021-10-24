from typing import *
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        cur=[]
        res=[]

        def dfs(used:List[bool], target:int ):
            level=len(cur)
            if level==target:
                res.append(cur.copy())
                return
            if level>target:
                return

            for i in range(0,len(nums)):
                if used[i]:
                    continue
                else:
                    used[i]=True
                    cur.append(nums[i])
                    dfs(used, target)
                    cur.pop()
                    used[i]=False
                    
        dfs([False]*len(nums),len(nums))
        return res

call=Solution()
print(call.permute([1,2,3]))