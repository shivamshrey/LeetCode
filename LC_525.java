// 525. Contiguous Array
// https://leetcode.com/problems/contiguous-array/

// TC: O(n)
// SC: O(n)

class Solution {
    public int findMaxLength(int[] nums) {
        // (count -> index) hashmap to track first occurrence of count value
        Map<Integer, Integer> hashmap = new HashMap<>();
        hashmap.put(0, -1);
        
        // count++ if nums[i] == 1
        // count-- if nums[i] == 0
        int count = 0;
        int result = 0;
        for (int i = 0; i < nums.length; i++) {
            count += nums[i] == 0 ? -1 : 1;
            
            if (hashmap.containsKey(count)) {
                result = Math.max(result, i - hashmap.get(count));
            } else {
                hashmap.put(count, i);
            }
        }
        return result;
    }
}
