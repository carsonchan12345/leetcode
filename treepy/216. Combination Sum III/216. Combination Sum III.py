from typing import *

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res=[]
        curr=[]
        candiate=[1,2,3,4,5,6,7,8,9]
        def dfs(sum:int, index:int):
            level=len(curr)
            if (level>k):
                return
            if (sum==n and level==k):
                res.append(curr.copy())
                return
            
            for i in range(index,len(candiate)):
                curr.append(candiate[i])
                dfs(sum+candiate[i],i+1)
                curr.pop()
        dfs(0,0)
        return res



call=Solution()
print(call.combinationSum3())