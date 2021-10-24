from typing import *
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        curr=[]
        candidates.sort()
        def dfs(index:int, sum:int):
            level=len(curr)

            if (sum>target):
                return
            if (sum==target):
                res.append(curr.copy())
                return
            prev=-1
            for i in range(index,len(candidates)):
                if candidates[i]==prev:
                    continue
                curr.append(candidates[i])
                dfs(i+1,sum+candidates[i])
                curr.pop()
                prev=candidates[i]
        dfs(0,0)
        return res

c= [10,1,2,7,6,1,5]
t=8
call=Solution()
print(call.combinationSum2(c,8))