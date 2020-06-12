class Solution {
    public int thirdMax(int[] nums) {
        
        long max = Long.MIN_VALUE;
        long secondMax = Long.MIN_VALUE;
        long thirdMax = Long.MIN_VALUE;
        
        for (int i = 0; i < nums.length; i++) {
            
            if (nums[i] > max) {
                thirdMax = secondMax;
                secondMax = max;
                max = nums[i];
            }
            else if (nums[i] == max)
                continue;
            else if (nums[i] > secondMax) {
                thirdMax = secondMax;
                secondMax = nums[i];
            }
            else if (nums[i] == secondMax)
                continue;
            else if (nums[i] > thirdMax)
                thirdMax = nums[i];
        }
        
        if (thirdMax == Long.MIN_VALUE)
            return (int)max;
        
        return (int)thirdMax;
    }
}