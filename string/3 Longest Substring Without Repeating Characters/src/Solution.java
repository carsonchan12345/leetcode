import java.util.HashSet;
import java.util.Set;

class Solution {
    public int lengthOfLongestSubstring(String s) {
        Set<Character> set = new HashSet<Character>();
        int max=0;
        int tmpmax=0;
        int tail=0, head=0;
        while(head<s.length()){
            if(set.contains(s.charAt(head)))
            {   System.out.println("test");
                tmpmax-=1;
                set.remove(s.charAt(tail));
                tail++;
            }
            else {
                tmpmax += 1;
                set.add(s.charAt(head));
                head++;
            }
            max=Math.max(max,tmpmax);
        }
        return max;
    }
}