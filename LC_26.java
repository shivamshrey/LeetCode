class Solution {
    public int removeDuplicates(int[] nums) {
        
        if (nums == null)
            return 0;
        
        int wp = 0;
        
        for (int rp = 1; rp < nums.length; rp++)
            if (nums[rp] > nums[wp])
                nums[++wp] = nums[rp];
        
        return wp + 1;
        
    }
}