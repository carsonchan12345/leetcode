public class main {
    public static void main (String[] args){
        String s = "AABABBA";
        String s2 = "ABAB";
        Solution call = new Solution();
        System.out.println(call.characterReplacement(s2, 2));
        System.out.println(call.characterReplacement(s, 1));
    }
}
