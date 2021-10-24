package Main;

import java.util.*;

class Solution {
    private int digitslen;
    private List<String> result;
    private String digits;

    public List<String> letterCombinations(String digits) {
        result = new ArrayList<String>();
        digitslen=digits.length();
        Convertedinit();
        this.digits=digits;
        treetraversal(0,"");
        return result;
    }
    //hash the number first
    private HashMap<String, String> Converted = new HashMap<String, String>();
    private void Convertedinit(){
        Converted.put("2","abc");
        Converted.put("3","def");
        Converted.put("4","ghi");
        Converted.put("5","jkl");
        Converted.put("6","mno");
        Converted.put("7","pqrs");
        Converted.put("8","tuv");
        Converted.put("9","wxyz");
    }

    private void treetraversal(int i, String currentstring)
    {   //check with the length, if the length is == digitslen, push to result list
        if (currentstring.length()==digitslen){
            result.add(currentstring);
            return;
        }
        Character tmp = digits.charAt(i);
        //recursion for the depth of the tree
        String convertedtmp = Converted.get(tmp.toString());
        for (int treelevel=0; treelevel<convertedtmp.length(); treelevel++){
            treetraversal(i+1, currentstring+convertedtmp.charAt(treelevel));
        }
    }
}