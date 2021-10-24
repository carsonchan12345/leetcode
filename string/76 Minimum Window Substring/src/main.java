public class main {
    public static void main (String[] args){
        String s = "ADOBECODEBANC";
        String t = "ABC";
        String s1 = "A";
        String t1 = "A";
        String s2 = "A";
        String t2 = "AA";
        String s3="bba";
        String t3="ab";
        Solution call = new Solution();
        System.out.println(call.minWindow(s,t));
        System.out.println(call.minWindow(s1,t1));
        System.out.println(call.minWindow(s2,t2));
        System.out.println(call.minWindow(s3,t3));

    }
}
