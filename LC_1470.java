class Solution {
    public int[] shuffle(int[] nums, int n) {
        int[] result = new int[2 * n];
        int i = 0, j = n, k = 0;
        
        while (k < 2 * n) {
            result[k++] = nums[i++];
            result[k++] = nums[j++];
        }
        
        return result;
    }
}
