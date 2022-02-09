// 532. K-diff Pairs in an Array
// https://leetcode.com/problems/k-diff-pairs-in-an-array/

// TC: O(n)
// SC: O(n)
class Solution {
    public int findPairs(int[] nums, int k) {
        int result = 0;
        Map<Integer, Integer> counts = new HashMap<>();
        for (int num : nums) {
            counts.put(num, counts.getOrDefault(num, 0) + 1);
        }
        
        for (Map.Entry<Integer, Integer> entry : counts.entrySet()) {
            if (k == 0 && counts.get(entry.getKey()) > 1 
                || k > 0 && counts.containsKey(entry.getKey() + k)) {
                result++;
            }
        }
        return result;
    }
}
