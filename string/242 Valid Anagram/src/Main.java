public class Main {
    public static void main (String[] args){
        String s ="anagram";
        String t ="nagaram";
        String s2 ="rat";
        String t2 ="car";
        Solution call = new Solution();
        System.out.println(call.isAnagram(s,t));
        System.out.println(call.isAnagram(s2,t2));


    }
}
