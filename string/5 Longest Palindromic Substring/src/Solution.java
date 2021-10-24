class Solution {
    public String longestPalindrome(String s) {
        int maxlength=0;
        String maxstring="";
        int l,r,tmplength;
        for(int i=0; i<s.length(); i++)
        {
            //odd
            l=i;
            r=i;
            tmplength=1;
            while(l>=0 && r<=s.length()-1 && s.charAt(l)==s.charAt(r))
            {
                if (tmplength>maxlength)
                {
                    maxlength=tmplength;
                    maxstring = s.substring(l,r+1);
                }
                l-=1;
                r+=1;
                tmplength+=2;
            }

            //even
            l=i;
            r=i+1;
            tmplength=2;
            while(l>=0 && r<=s.length()-1 && s.charAt(l)==s.charAt(r))
            {
                if (tmplength>maxlength)
                {
                    maxlength=tmplength;
                    maxstring = s.substring(l,r+1);
                }
                l-=1;
                r+=1;
                tmplength+=2;
            }

        }
        return maxstring;
    }
}