class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        visited=set()
        adjList={}
        for course in prerequisites:
            if course[0]==course[1]:
                return False
            if (course[0] not in adjList):
                adjList[course[0]]=[course[1]]
            else:
                adjList[course[0]].append(course[1])
            
        def dfs(course:int) -> bool:
            if course not in adjList:
                return True
            if course in visited:
                print("visited",course, visited)
                return False
            visited.add(course)

            for x in adjList[course]:
                if not dfs(x):
                    return False
            visited.remove(course)
            adjList.pop(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True