class Solution {
    public int search(int[] nums, int target) {
        int head = nums.length-1;
        int tail = 0;
        int index=-1;
        int i=1;

        while (tail<=head){
            int mid = (tail + (head) )/2;

            if (nums[mid]==target){
                index=mid;
                return index;
            }

            if (nums[mid]>=nums[tail]){
                if (target<nums[tail] || target>nums[mid])
                    tail=mid+1;
                else
                    head=mid-1;
            }
            else if (target<nums[mid] || target>nums[head]){
                head=mid-1;
            }
            else tail=mid+1;

            System.out.println("loop"+i);
            System.out.println("mid"+nums[mid]);
            System.out.println("index"+index);
            System.out.println("tail"+tail+" head"+head);
            i++;
        }

        return index;
    }
}