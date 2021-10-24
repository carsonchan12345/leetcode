# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional


class Solution:
    smallest:int
    nth:int
    def __init__(self):
        self.smallest=0
        self.nth=0

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.nth=root.val
        self.recur(root,k)
        return self.nth

    def recur(self, root: Optional[TreeNode], k:int) -> bool:
        if not root:
            return True
        left = self.recur(root.left,k)
        if (left==False):
            return False
        self.smallest+=1
        if self.smallest==k:
            self.nth=root.val
            return False
        right= self.recur(root.right,k)

        return True



