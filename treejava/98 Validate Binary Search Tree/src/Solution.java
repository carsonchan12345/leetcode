/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean isValidBST(TreeNode root) {

        return checkLayer(root,null,null);

    }

    private boolean checkLayer(TreeNode root, Integer left_limit, Integer right_limit){

        if (root == null)
            return true;
        if (root.left!=null){
            if (root.left.val>=root.val)
                return false;
            if (left_limit!=null){
                if (root.left.val<=left_limit)
                    return false;
            }
        }
        if (root.right!=null){
            if (root.right.val<=root.val)
                return false;
            if (right_limit!=null){
                if (root.right.val>=right_limit)
                    return false;
            }
        }
            return checkLayer(root.left,left_limit,Integer.valueOf(root.val)) &&  checkLayer(root.right,Integer.valueOf(root.val),right_limit);

    }
}