// 18. 4Sum
// https://leetcode.com/problems/4sum/

// TC: O(n^3)
// SC: O(1)
class Solution {
    public List<List<Integer>> fourSum(int[] nums, int target) {
        Arrays.sort(nums);
        int n = nums.length;
        List<List<Integer>> ans = new ArrayList<>();
        
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                int l = j + 1, r = n - 1;
                int remain = target - nums[i] - nums[j];
                while (l < r) {
                    if (nums[l] + nums[r] == remain) {
                        ans.add(Arrays.asList(nums[i], nums[j], nums[l], nums[r]));
                        // Skip duplicate nums[l]
                        while (l < r && nums[l + 1] == nums[l]) ++l;
                        ++l;
                        while (l < r && nums[r - 1] == nums[r]) --r;
                        --r;
                    } else if (nums[l] + nums[r] > remain) {
                        while (l < r && nums[r - 1] == nums[r]) --r;
                        --r;
                    } else {
                        while (l < r && nums[l + 1] == nums[l]) ++l;
                        ++l;
                    }
                }
                // Skip duplicate nums[j]
                while (j + 1 < n && nums[j] == nums[j + 1]) ++j; 
            }
            // Skip duplicate nums[i]
            while (i + 1 < n && nums[i] == nums[i + 1]) ++i; 
        }
        return ans;
    }
}
