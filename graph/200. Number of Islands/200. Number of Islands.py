from typing import *
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        res=0
        bfs=[]
        visited=set()
        rowLength=len(grid)
        colLength=len(grid[0])

        for row in range(rowLength):
            for col in range(colLength):
                if ((row,col) not in visited) and grid[row][col]=='1':
                    res+=1
                    bfs.append([row,col])
                    visited.add((row,col))

                    while(bfs):
                        tmp=bfs.pop(0)
                        r=tmp[0]
                        c=tmp[1]

                        if (c>0 and (r,c-1) not in visited and grid[r][c-1]=='1') :
                            bfs.append([r,c-1])
                            visited.add((r,c-1))
                        if (c<colLength-1 and (r,c+1) not in visited and grid[r][c+1]=='1') :
                            bfs.append([r,c+1])
                            visited.add((r,c+1))
                        if (r>0 and (r-1,c) not in visited and grid[r-1][c]=='1') :
                            bfs.append([r-1,c])
                            visited.add((r-1,c))
                        if (r<rowLength-1 and (r+1,c) not in visited and grid[r+1][c]=='1') :
                            bfs.append([r+1,c])
                            visited.add((r+1,c))
        return res

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
call=Solution()
print(call.numIslands(grid))


