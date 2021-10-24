# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def __init__(self):
        self.res:TreeNode

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.res=root
        tmp=self.recur(root,p,q)
        return self.res
    
    def recur(self, root:Optional[TreeNode], p:TreeNode, q:TreeNode) -> bool:
        if not root:
            return False
        
        left=self.recur(root.left,p,q)
        right=self.recur(root.right,p,q)
        
        if (left and right or (root.val==p.val or root.val==q.val) and (left or right) ):
            self.res=root
            return False
        
        return root.val==p.val or root.val==q.val or left or right

