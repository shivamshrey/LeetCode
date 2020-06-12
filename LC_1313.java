class Solution {
    public int[] decompressRLElist(int[] nums) {
        
        int size = 0;
        for (int i = 0; i < nums.length; i += 2)
            size += nums[i];
        
        int[] result = new int[size];
		int j = 0;
		
		for (int i = 0; i < nums.length; i += 2) {
			Arrays.fill(result, j, j + nums[i], nums[i + 1]);
            j += nums[i];
		}
		
		return result;
    }
}