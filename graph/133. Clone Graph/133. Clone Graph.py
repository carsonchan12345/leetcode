"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return
        bfs=[]
        bfs.append(node)
        oldToNew={}
        visited=set()
        while(bfs):
            curr=bfs.pop()
            if curr.val not in oldToNew:
                oldToNew[curr.val]=Node(curr.val)
            if curr.val not in visited:
                visited.add(curr.val)
            else:
                continue

            for neighbor in curr.neighbors:
                if neighbor.val not in oldToNew:
                    oldToNew[neighbor.val]=Node(neighbor.val)
                oldToNew[curr.val].neighbors.append(oldToNew[neighbor.val])
                if neighbor.val not in visited:
                    bfs.append(neighbor)
        return oldToNew[node.val]
                
