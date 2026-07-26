class Solution {
    public int maxProfit(int[] prices) {
        int profit=0;
        for(int day=0;day<prices.length-1;day++){
            if(prices[day] <prices[day+1]){
                profit+=Math.abs(prices[day]-prices[day+1]);
            }
        }
        return profit;

    }
}