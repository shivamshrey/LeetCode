// 309. Best Time to Buy and Sell Stock with Cooldown

// TC: O(n)
// SC: O(n)

class Solution {
    public int maxProfit(int[] prices) {
        int[] noStock = new int[prices.length];
        int[] hold = new int[prices.length];
        int[] sold = new int[prices.length];
        
        noStock[0] = 0;                 // don't have it on day 0
        hold[0] = 0 - prices[0];        // buying/holding it on day 0
        sold[0] = Integer.MIN_VALUE;    // selling on day 0
        
        for (int i = 1; i < prices.length; i++) {
            noStock[i] = Math.max(noStock[i - 1], sold[i - 1]);
            hold[i] = Math.max(hold[i - 1], noStock[i - 1] - prices[i]);
            sold[i] = hold[i - 1] + prices[i];
        }
        
        return Math.max(noStock[prices.length - 1], sold[prices.length - 1]);
    }
}
