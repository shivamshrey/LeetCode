// 33. Search in Rotated Sorted Array

class Solution {
    public int search(int[] nums, int target) {
        int low = 0, high = nums.length - 1;
        
        while (low <= high) {
            int mid = low + (high - low) / 2;
            
            int num = nums[mid];
            // if nums[mid] and target are "on the same side" of nums[0]
            if ((nums[mid] < nums[0]) == (target < nums[0])) {
                num = nums[mid];
            } else {
                num = target < nums[0] ? Integer.MIN_VALUE : Integer.MAX_VALUE;
            }
            
            if (num < target)
                low = mid + 1;
            else if (num > target)
                high = mid - 1;
            else
                return mid;
        }
        
        return -1;
    }
}
