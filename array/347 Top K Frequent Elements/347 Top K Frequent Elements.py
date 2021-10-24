import heapq as hq
from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        res=[]
        for x in nums:
            if x not in freq:
                freq[x]=1
            else:
                freq[x]+=1
        freq=list(freq.items())
        freq.sort(key = lambda x: x[1], reverse=True)
        for i in range(k):
            
            res.append(freq[i][0])
        




class main:
    call = Solution()
    list =[1,1,1,2,2,3]
    k=2
    call.topKFrequent(list,k)


if __name__ == '__main__':
    main()
