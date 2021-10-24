# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[]
        tmp=[]
        
        queue=[]
        queue.append(root)
        if not root:
            return []
        while queue:
            for i in range(len(queue)):
                tmp2 = queue.pop(0)
                tmp.append(tmp2.val)
                if tmp2.left:
                    queue.append(tmp2.left)
                if tmp2.right:
                    queue.append(tmp2.right)
            res.append(tmp)
            tmp=[]
        return res
            