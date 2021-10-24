public class main {

    public static void main(String[] args){
        int[] nums= {3,2,4};
        Solution call = new Solution();
        int[] result=call.twoSum(nums, 6);
        System.out.print("["+result[1]+","+result[0]+"]");

    }
}
