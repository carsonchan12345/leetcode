class Solution {
    public int maxSubArray(int[] nums) {
        int result=nums[0];
        int tmpresult=0;
        for (int i=0; i<nums.length; i++){
            tmpresult+=nums[i];
            if (tmpresult>result)
                result=tmpresult;
            if (tmpresult<0)
            {
                tmpresult=0;
            }
        }
        return result;
    }
}