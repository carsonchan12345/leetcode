public class main {
    public static void main (String [] args){
        int[] height = {1,8,6,2,5,4,8,3,7};
        int[] height2 = {4,3,2,1,4};
        int[] height3 = {1,2,1};

        Solution call = new Solution();
        System.out.println(call.maxArea(height));
        System.out.println(call.maxArea(height2));
        System.out.println(call.maxArea(height3));

    }
}
