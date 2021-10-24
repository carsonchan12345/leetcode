import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {

    public List<List<Integer>> threeSum(int[] nums) {
        int tail;
        int head;
        List <List<Integer>> res = new ArrayList<List<Integer>>();
        Arrays.sort(nums);

        for (int i=0; i<nums.length; i++){
            if (i>0 && nums[i]==nums[i-1])
                continue;
            tail=i+1;
            head=nums.length-1;
            System.out.println(nums + "loop i");
            while (head>tail)
            {   System.out.println(tail +" "+head);
                if (nums[i]+nums[tail]+nums[head] == 0) {
                    res.add(Arrays.asList(nums[i], nums[tail], nums[head]));
                    tail++;
                    while(nums[tail]==nums[tail-1] && head>tail)
                        tail++;
                }
                else if (nums[i]+nums[tail]+nums[head] > 0)
                    head--;
                else tail++;
            }
        }
        return res;
    }

    public static void main (String[] args){
        int [] nums ={-1, 0,1,2,-1,4};
        int [] nums2 ={0,0,0};
        Solution call = new Solution();
        List<List<Integer>> res = call.threeSum(nums);
        List<List<Integer>> res2 = call.threeSum(nums2);

        System.out.println(res);
        System.out.println(res2);

    }
}