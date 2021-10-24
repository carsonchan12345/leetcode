import heapq
class MedianFinder:
    
    def __init__(self):
        self.left=[]
        self.right=[]

    def addNum(self, num: int) -> None:
        if not self.left:
            heapq.heappush(self.left,0-num)
        elif num<0-heapq.nsmallest(1,self.left)[0]:
            heapq.heappush(self.left,0-num)
        else:
            heapq.heappush(self.right,num)
        print('lr',self.left, self.right)
        if (len(self.right)>len(self.left)):
            heapq.heappush(self.left,0-heapq.heappop(self.right))
        elif len(self.left)>len(self.right)+1:
            heapq.heappush(self.right,0-heapq.heappop(self.left))
        print('lr',self.left, self.right)
        
    def findMedian(self) -> float:

        if len(self.right)==len(self.left):
            return (0-heapq.nsmallest(1,self.left)[0]+heapq.nsmallest(1,self.right)[0])/2
        else:
            return 0-heapq.nsmallest(1,self.left)[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


# import heapq
# class MedianFinder:
    
#     def __init__(self):
#         self.res=[]
#         self.length=0

#     def addNum(self, num: int) -> None:
#         self.res.append(num)
#         self.length+=1

#     def findMedian(self) -> float:
#         self.res.sort()
#         if self.length%2==0:
#             return (self.res[int(self.length/2)] + self.res[int(self.length/2)-1])/2
#         else:
#             return self.res[int(self.length/2)]


# # Your MedianFinder object will be instantiated and called as such:
# # obj = MedianFinder()
# # obj.addNum(num)
# # param_2 = obj.findMedian()