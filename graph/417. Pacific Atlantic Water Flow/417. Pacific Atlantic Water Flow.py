from typing import *
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        res=[]

        visited=set()

        self.pac_reach=False
        self.alt_reach=False

        def dfs(x:int, y:int):
            if (x,y) in visited:
                return False
            if x==0 or y==0:
                self.pac_reach=True
            if x==len(heights[0])-1 or y==len(heights)-1:
                self.alt_reach=True
            if self.pac_reach and self.alt_reach:
                return True
            visited.add((x,y))
            print(x,y)
            if (x>0 and heights[y][x]>=heights[y][x-1]):
                if (dfs(x-1,y)):
                    visited.remove((x,y))
                    return True
            if (x<len(heights[0])-1 and heights[y][x]>=heights[y][x+1]):
                if (dfs(x+1,y)):
                    visited.remove((x,y))
                    return True
            if (y>0 and heights[y][x]>=heights[y-1][x]):
                if (dfs(x,y-1)):
                    visited.remove((x,y))
                    return True
            if (y<len(heights)-1 and heights[y][x]>=heights[y+1][x]):
                if (dfs(x,y+1)):
                    visited.remove((x,y))
                    return True

            visited.remove((x,y))
            return False
        
        
        for y in range(len(heights)):
            for x in range(len(heights[0])):
                self.pac_reach=False
                self.alt_reach=False
                print("st")
                if dfs(x,y):
                    res.append([y,x])
        
        return res

call=Solution()
print(call.pacificAtlantic([[1,1],[1,1],[1,1]]))                    