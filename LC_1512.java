class Solution {
    public int numIdenticalPairs(int[] nums) {
        int count = 0, i = 0;
        Arrays.sort(nums);
        
        for (int j = 1; j < nums.length; j++) {
            if (nums[i] == nums[j])
                count += j - i;
            else
                i = j;
        }
        
        return count;
    }
}
