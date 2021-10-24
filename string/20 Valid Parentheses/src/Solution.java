import java.util.HashMap;
import java.util.HashSet;
import java.util.Stack;

class Solution {
    public boolean isValid(String s) {
        Stack <Character> res = new Stack<>();
        HashMap<Character, Character> par = new HashMap<>();
        par.put('(',')');
        par.put('{','}');
        par.put('[',']');

        for (int i=0; i<s.length(); i++)
        {
            if (par.containsKey(s.charAt(i)))
            {
                res.push(s.charAt(i));
            }
            else
            {
                if (res.isEmpty())
                    return false;
                if (par.get(res.pop())!=s.charAt(i))
                    return false;
            }
        }
        return res.isEmpty();
    }
}