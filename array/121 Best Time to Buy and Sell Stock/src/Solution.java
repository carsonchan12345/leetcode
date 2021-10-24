class Solution {
    public int maxProfit(int[] prices) {
        int pointer1=0;
        int pointer2=1;
        int maxprofit=0;

        for (int i=0; i<prices.length-1; i++){
            if (prices[pointer2]>prices[pointer1]) {
                int tmpprofit=prices[pointer2]-prices[pointer1];
                if  (tmpprofit> maxprofit){
                maxprofit=tmpprofit;
                }
            pointer2++;
            }
            else {
                pointer1 = i + 1;
                pointer2++;
            }
        }
        return maxprofit;
    }
}