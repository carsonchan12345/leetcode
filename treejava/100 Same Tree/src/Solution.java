class Solution {
    public boolean isSameTree(TreeNode root, TreeNode subRoot){
        if (root == null && subRoot ==null)
  {      
            System.out.print("yesnull");
            return true;}
        
        if ( root==null || subRoot==null||root.val!= subRoot.val )
            return false;
        
        return isSameTree(root.left, subRoot.left) && isSameTree(root.left, subRoot.right);
    }
    
}