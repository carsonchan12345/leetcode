public class main {

    public static void main(String[] args){
        int[] nums={-1,1,0,-3,3};
        Solution call= new Solution();
        int[] result = call.productExceptSelf(nums);
        for (int integer:result){
            System.out.println(integer);
        }
    }
}
