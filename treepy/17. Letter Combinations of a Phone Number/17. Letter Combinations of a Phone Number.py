from typing import *
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        keyDict={'2':'abc', '3': 'def', '4': 'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        curr=""
        res=[]

        def dfs(level:int,curr:str):

            if level==len(digits):
                res.append(curr)
                return
            
            tmp=keyDict[digits[level]]
            print(curr)
            for c in tmp:
                curr+=c
                dfs(level+1,curr)
                curr=curr[:len(curr)-1]
        if len(digits)==0:
            return res
        dfs(0,curr)
        return res



call=Solution()
print(call.letterCombinations("23"))