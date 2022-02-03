// 454. 4Sum II
// https://leetcode.com/problems/4sum-ii/

// TC: O(n^2)
// SC: O(n^2)
class Solution {
    public int fourSumCount(int[] nums1, int[] nums2, int[] nums3, int[] nums4) {
        Map<Integer, Integer> hashmap = new HashMap<>();
        int result = 0;
        for (int i = 0; i < nums1.length; i++) {
            for (int j = 0; j < nums2.length; j++) {
                hashmap.put(nums1[i] + nums2[j],
                            hashmap.getOrDefault(nums1[i] + nums2[j], 0) + 1);
            }
        }
        
        for (int k = 0; k < nums3.length; k++) {
            for (int l = 0; l < nums3.length; l++) {
                result += hashmap.getOrDefault(-(nums3[k] + nums4[l]), 0);
            }
        }
        return result;
    }
}
