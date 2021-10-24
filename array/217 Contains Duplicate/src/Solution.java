import java.util.HashSet;
import java.util.Set;

class Solution {//o(n)
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> numset = new HashSet<Integer>();

        for(int integer: nums) {
            if (numset.contains(integer))
                return true;
            else {
                numset.add(integer);
            }
        }
        return false;
    }
}