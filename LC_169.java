// 169. Majority Element

class Solution {
    public int majorityElement(int[] nums) {
        int result = nums[0];
        int count = 1;
        
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] == result)
                count++;
            else
                count--;
            if (count == 0) {
                count = 1;
                result = nums[i];
            }
        }
        
        return result;
    }
}
