class Solution {
    public int maxProduct(int[] nums) {
        
        int max = Integer.MIN_VALUE;
        int secondMax = Integer.MIN_VALUE;
        int maxIndex = 0, secondMaxIndex = 0;
        
        for (int i = 0; i < nums.length; i++) {
            
            if (nums[i] > max) {
                secondMax = max;
                secondMaxIndex = maxIndex;
                max = nums[i];
                maxIndex = i;
            } else if (nums[i] > secondMax || (nums[i] == max && nums[i] > secondMax)) {
                secondMax = nums[i];
                secondMaxIndex = i;
            }
        }
        
        return (nums[maxIndex] - 1) * (nums[secondMaxIndex] - 1);
    }
}