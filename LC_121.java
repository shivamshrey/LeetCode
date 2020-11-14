// 121. Best Time to Buy and Sell Stock

class Solution {
    public int maxProfit(int[] prices) {
		if (prices == null || prices.length == 0)
			return 0;

        int minprice = Integer.MAX_VALUE;
        int maxprofit = 0;
        
        for(int i = 1; i < prices.length; i++){
            if(prices[i] > prices[i - 1]){
                minprice = Math.min(prices[i-1], minprice);
                maxprofit = Math.max(maxprofit, prices[i] - minprice);
            }
        }
		
        return maxprofit;
    }
}
