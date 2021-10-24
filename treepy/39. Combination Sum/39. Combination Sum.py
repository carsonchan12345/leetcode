from typing import *

class Solution:

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        cur=[]
        res=[]
        
        def dfs(i:int, sum:int):
            if sum>target:
                return
            if sum==target:
                print(cur,sum)
                res.append(cur.copy())
            for x in range(i,len(candidates)):
                cur.append(candidates[x])
                dfs(x, sum+candidates[x])
                cur.pop()
        
        dfs(0, 0)
        return res
# from typing import *

# class Solution:

#     def __init__(self) -> None:
#         pass
#     def combinationSum4(self, nums: List[int], target: int) -> int:
#         dp={0:1}

#         for total in range(1,target+1):
#             dp[total]=0
#             for n in nums:
#                 dp[total]+=dp.get(total-n,0)
#         return dp[total]
    

so=Solution()
c= [2,3,6,7]
t=7
print(so.combinationSum(c,t))