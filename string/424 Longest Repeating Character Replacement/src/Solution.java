
import java.util.HashMap;
import java.util.Collections;
class Solution {
    public int characterReplacement(String s, int k) {
        int head = 0, tail = 0;
        int max=0, tmpmax=0;
        HashMap<Character, Integer> dict = new HashMap<Character, Integer>();
        while(head<s.length()){
            if (dict.putIfAbsent(s.charAt(head), 1)!=null){
                dict.computeIfPresent(s.charAt(head),(key,val) -> val+=1);
            }
            System.out.println(dict.keySet()+" "+dict.values()+" "+tmpmax);
            tmpmax++;
            while(k<tmpmax-Collections.max(dict.values())) {
                dict.computeIfPresent(s.charAt(tail), (key, val) -> val -=1);
                tail++;
                tmpmax--;
            }
            head++;
            max = Math.max(max, tmpmax);
        }
        return  max;
    }
}