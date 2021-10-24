class Solution {
    public int countSubstrings(String s) {

        int l, r, count = 0;
        for (int i = 0; i < s.length(); i++) {
            //odd
            l = i;
            r = i;
            while (l >= 0 && r <= s.length() - 1 && s.charAt(l) == s.charAt(r)) {
                count++;
                l -= 1;
                r += 1;
            }

            //even
            l = i;
            r = i + 1;
            while (l >= 0 && r <= s.length() - 1 && s.charAt(l) == s.charAt(r)) {
                count++;
                l -= 1;
                r += 1;
            }

        }
        return count;
    }
}
