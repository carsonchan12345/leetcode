from typing import *

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList={}
        visited=set()
        res=[]
        for x in prerequisites:
            if x[0]==x[1]:
                return False
            if x[0] not in adjList:
                adjList[x[0]]=[x[1]]
            else:
                adjList[x[0]].append(x[1])

        def dfs(course:int)-> bool:
            if course not in adjList:
                if course not in visited:
                    print(course)
                    res.append(course)
                visited.add(course)
                return True
            
            if course in visited:
                return False
            visited.add(course)

            for x in adjList[course]:
                if not dfs(x):
                    return False
            res.append(course)
            adjList.pop(course)

            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return []
        return res
        
numCourses = 2
prerequisites = [[0,1],[1,0]]
call=Solution()
print(call.findOrder(numCourses, prerequisites))

            