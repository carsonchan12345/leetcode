import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;

class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String,List<String>> res = new HashMap<>();
        for (String s : strs)
        {
            char tmp[] = s.toCharArray();
            Arrays.sort(tmp);
            if (res.containsKey(new String(tmp)))
            {
                res.get(new String(tmp)).add(s);
            }
            else
            {
                res.put(new String(tmp), new ArrayList<String>(Arrays.asList(s)));
            }
        }
        return new ArrayList<List<String>>(res.values());
    }

}