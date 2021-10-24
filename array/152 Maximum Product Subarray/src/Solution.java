import java.util.Arrays;
import java.util.Collection;
import java.util.Collections;
import java.util.List;

class Solution {

    private int findMax(int[] nums){
        int tmp=nums[0];
        for (int i : nums){
            tmp=Math.max(tmp, i);
        }
        return tmp;
    }

    public int maxProduct(int[] nums) {

        int res = findMax(nums);
        int min = 1;
        int max = 1;
        for (int i=0; i<nums.length; i++){
            if (nums[i]==0) {
                min = 1;
                max = 1;
                continue;
            }
            int curtmp= max * nums[i];
            List<Integer> tmp = Arrays.asList(new Integer[]{nums[i], max * nums[i], min * nums[i]});
            max= Collections.max(tmp);
            tmp = Arrays.asList(new Integer[]{nums[i], curtmp, min * nums[i]});
            min= Collections.min(tmp);
            res=Math.max(res, max);
        }
        return res;
    }
}