from typing import *
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res=0
        curr=0
        hash =set()
        for x in nums:
            hash.add(x)
        
        for x in nums:
            if x-1 not in hash:
                curr=1
                tmp=x
                while(tmp+1 in hash):
                    curr+=1
                    tmp+=1
                res=max(curr,res)
        return res
nums = [0,3,7,2,5,8,4,6,0,1]
call=Solution()
print(call.longestConsecutive(nums))
