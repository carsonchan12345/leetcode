import java.util.HashMap;

class Solution {
    public boolean isAnagram(String s, String t) {
        int need=0, have=0;
        HashMap<Character, Integer> need_dict = new HashMap<>();
        HashMap<Character, Integer> search_dict = new HashMap<>();

        if (s.length()!=t.length())
            return false;

        for(int i=0; i<t.length(); i++){
            if (need_dict.get(t.charAt(i))==null)
                need_dict.put(t.charAt(i), 1);
            else
                need_dict.put(t.charAt(i), need_dict.get(t.charAt(i))+1);

            search_dict.put(t.charAt(i), 0);
            need++;
        }

        for(int i=0; i<s.length(); i++)
        {   Character tmp=s.charAt(i);
            if (need_dict.get(tmp)==null)
                return false;
            if (search_dict.get(tmp)<need_dict.get(tmp))
            {
                have++;
            }
            else return false;
            search_dict.put(tmp, search_dict.get(tmp)+1) ;
        }
        return (have==need);
    }
}
//class Solution {
//    public boolean isAnagram(String s, String t) {
//        int need=0, have=0;
//        HashMap<Character, Integer> need_dict = new HashMap<>();
//        HashMap<Character, Integer> search_dict = new HashMap<>();
//
//        if (s.length()!=t.length())
//            return false;
//
//        char tmpct[] = t.toCharArray();
//        Arrays.sort(tmpct);
//        String tmpt = new String(tmpct);
//
//        char tmpcs[] = s.toCharArray();
//        Arrays.sort(tmpcs);
//        String tmps = new String(tmpcs);
//        System.out.println(tmpt+" "+tmps);
//        return (tmps.equals(tmpt));
//    }
//}