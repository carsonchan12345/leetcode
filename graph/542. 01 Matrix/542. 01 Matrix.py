from typing import *
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        dist=[[-1,0],[1,0],[0,-1],[0,1]]
        bfs=[]
        visited=set()
        res=mat.copy()
        ROW=len(mat)
        COL=len(mat[0])
        for row in range(ROW):
            for col in range(COL):
                if res[row][col] == 1:
                    res[row][col]=-1
                if res[row][col]==0:
                    bfs.append([row,col])

        while(bfs):
            tmp=bfs.pop(0)
            r=tmp[0]
            c=tmp[1]

            for d in dist:
                tmpr=r+d[0]
                tmpc=c+d[1]
                if (tmpc<0 or tmpr<0 or tmpc==COL or tmpr==ROW):
                    continue
                if res[tmpr][tmpc]>res[r][c]+1 or res[tmpr][tmpc]==-1:
                    res[tmpr][tmpc]=res[r][c]+1
                    bfs.append([tmpr,tmpc])
        return res
mat = [[0,1,0,1,1],[1,1,0,0,1],[0,0,0,1,0],[1,0,1,1,1],[1,0,0,0,1]]
call=Solution()
print(call.updateMatrix(mat))