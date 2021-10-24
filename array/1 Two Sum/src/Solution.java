import java.util.HashMap;
import java.util.Map;


class Solution {

    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> hash_Set = new HashMap<Integer, Integer>();
        int result[] = new int[2];
        int index=0;
        for(int integer:nums) {
            if (hash_Set.containsKey(target-integer)) {
                result[0] = hash_Set.get(target - integer);
                break;
            }
            hash_Set.put(integer,index);
            index++;
        }
        System.out.println(hash_Set);

        result[1]=index;
        return result;
    }
}