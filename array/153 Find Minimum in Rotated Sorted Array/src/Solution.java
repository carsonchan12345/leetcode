class Solution {
    public int findMin(int[] nums) {
        int head = nums.length-1;
        int tail = 0;
        int minimum=nums[0];
        int i=1;
        while (tail<=head){
            int mid = (tail + (head+1) )/2;

            if (nums[mid]<minimum)
                minimum=nums[mid];

            if (nums[0]<nums[mid])
                tail=mid+1;
            else
                head=mid-1;
            System.out.println("loop"+i);
            System.out.println("mid"+nums[mid]);
            System.out.println("mini"+minimum);
            i++;
        }
        return minimum;
    }
}