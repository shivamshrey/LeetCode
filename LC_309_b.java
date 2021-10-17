// 309. Best Time to Buy and Sell Stock with Cooldown

// TC: O(n)
// SC: O(1)

class Solution {
    public int maxProfit(int[] prices) {        
        int noStock = 0;                 // don't have it on day 0
        int hold = 0 - prices[0];        // buying/holding it on day 0
        int sold = Integer.MIN_VALUE;    // selling on day 0
        
        for (int i = 1; i < prices.length; i++) {
            int prevNoStock = noStock;
            int prevHold = hold;
            int prevSold = sold;
            noStock = Math.max(prevNoStock, prevSold);
            hold = Math.max(hold, prevNoStock - prices[i]);
            sold = prevHold + prices[i];
        }
        
        return Math.max(noStock, sold);
    }
}
