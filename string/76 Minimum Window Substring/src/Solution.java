import java.util.HashMap;

class Solution {
    public String minWindow(String s, String t) {
        HashMap<Character, Integer> need_dict = new HashMap<>();
        int need=0;
        HashMap<Character, Integer> search_dict = new HashMap<>();
        int have=0;
        int minlength=s.length()+1;
        int tmplength=0;
        int tail=0;
        int[] headntail= {-1,-1};
        for(int i=0; i<t.length(); i++){
            if (need_dict.putIfAbsent(t.charAt(i), 1)!=null)
                need_dict.computeIfPresent(t.charAt(i),(key, val)-> val+=1);
            search_dict.putIfAbsent(t.charAt(i), 0);
            need++;
        }
        System.out.println(need_dict);
        for(int i=0; i<s.length();i++){
            tmplength++;
            if (need_dict.containsKey(s.charAt(i))){
                if (search_dict.get(s.charAt(i)) < need_dict.get(s.charAt(i)))
                {
                    have++;
                }
                search_dict.compute(s.charAt(i),(key, val)-> val+=1);
            }
            System.out.println(have +" "+need);
            System.out.println("Search: " + search_dict);
            while (need==have)
            {
                if(tmplength < minlength)
                {
                    headntail[0]=tail;
                    headntail[1]=i;
                    minlength=tmplength;
                }
                if (need_dict.containsKey(s.charAt(tail)))
                {
                    search_dict.compute(s.charAt(tail),(k,v)-> v-=1);
                    if (search_dict.get(s.charAt(tail)) < need_dict.get(s.charAt(tail)))
                        have--;
                }
                tail++;
                tmplength--;
            }
        }
        System.out.println(headntail[0] +" "+headntail[1]);
        if (headntail[0]!=-1)
            return s.substring(headntail[0],headntail[1]+1);
        else
            return "";

    }
}