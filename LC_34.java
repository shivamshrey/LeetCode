class Solution {
    public int[] searchRange(int[] nums, int target) {
        int low = 0;
        int high = nums.length - 1;
        int left = -1;
        int right = -1;
        
        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (target <= nums[mid])
                high = mid - 1;
            else
                low = mid + 1;
            
            left = (nums[mid] == target) ? mid : left;            
        }
        
        low = 0;
        high = nums.length - 1;
        
        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (target >= nums[mid])
                low = mid + 1;
            else
                high = mid - 1;
            
            right = (nums[mid] == target) ? mid : right;            
        }
        
        return new int[]{left, right};
    }
}
