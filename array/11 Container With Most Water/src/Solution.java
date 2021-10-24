class Solution {
    public int maxArea(int[] height) {
        int tail=0;
        int head=height.length-1;
        int res=0;
        while(head>tail){
            res=Math.max(res, (head-tail) * Math.min(height[tail],height[head]));
            if (height[tail]>height[head])
                head--;
            else
                tail++;
        }
        return res;
    }
}