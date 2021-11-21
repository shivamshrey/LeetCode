// 673. Number of Longest Increasing Subsequence

class Solution {
    public int findNumberOfLIS(int[] nums) {
        int[] lis = new int[nums.length];   // lis[i] = length of LIS ending at i
        int[] counts = new int[nums.length];    // counts[i] = count of LIS ending at i
        Arrays.fill(lis, 1);
        Arrays.fill(counts, 1);
        
        int maxLen = 1; // length of LIS
        for (int i = 1; i < nums.length; i++) {
            for (int j = 0; j < i; j++) {
                if (nums[j] < nums[i]) {
                    if (lis[j] + 1 > lis[i]) {    // strictly increasing
                        lis[i] = lis[j] + 1;
                        counts[i] = counts[j];
                    } else if (lis[j] + 1 == lis[i]) {
                        counts[i] += counts[j];
                    }
                }
            }
            maxLen = Math.max(maxLen, lis[i]);
        }
        
        int result = 0;
        
        for (int i = 0; i < nums.length; i++) {
            if (lis[i] == maxLen)
                result += counts[i];
        }
        
        return result;
    }
}
