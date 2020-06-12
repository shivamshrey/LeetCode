class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        
        int count = 0, max = 0;
        
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 1) {
                if (++count > max)
                    max = count;
            } else
				count = 0;
        }
        
        return max;
        
    }
}