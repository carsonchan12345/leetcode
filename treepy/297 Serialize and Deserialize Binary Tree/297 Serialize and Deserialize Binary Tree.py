# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
                :type root: TreeNode
        :rtype: str
        """
        
        q =[]
        tmp=[]
        res =[]
        if not root:
            return ""
        q.append(root)
        while q:
            for i in range(len(q)):
                tmp2=q.pop(0)
                
                if tmp2:
                    res.append(tmp2.val)
                    q.append(tmp2.left)
                    q.append(tmp2.right)
                else:
                    res.append(tmp2)
        tmp=str(',').join([str(s) for s in res])
        print(tmp)
        return tmp
        


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        q1=[]
        if not data:
            return 
        data=data.split(',')
        root=TreeNode(data.pop(0))
        q1.append(root)
        while q1:
            tmp=q1.pop(0)
            if not tmp.left:
                tmp2=data.pop(0)
                if tmp2=="None":
                    tmp2=None
                else:
                    tmp.left=TreeNode(tmp2)
                if tmp2:
                    q1.append(tmp.left)
            if not tmp.right:
                tmp2=data.pop(0)
                if tmp2=='None':
                    tmp2=None
                else:
                    tmp.right=TreeNode(tmp2)
                if tmp2:
                    q1.append(tmp.right)
        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))