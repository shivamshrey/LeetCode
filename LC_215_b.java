// 215. Kth Largest Element in an Array

// TC: O(n)
// SC: O(1)

class Solution {
    public int findKthLargest(int[] nums, int k) {
        int low = 0, high = nums.length - 1, p = 0;
        
        while (low <= high) {
            p = partition(nums, low, high);
            if (p == k - 1)
                break;
            else if (p < k - 1)
                low = p + 1;
            else
                high = p - 1;
        }
        return nums[p];       
    }
    
    private int partition(int[] nums, int low, int high) {
        // Using Lomuto partition scheme
        // Randomizing pivot
        int randomIndex = ThreadLocalRandom.current().nextInt(low, high + 1);
        swap(nums, randomIndex, high);
        int pivot = nums[high];
        int i = low;
        
        for (int j = low; j < high; j++) {
            if (nums[j] > pivot) {
                swap(nums, i, j);
                i++;
            }
        }
        swap(nums, i, high);
        return i;
    }
    
    private void swap(int[] nums, int i, int j) {
        // swap nums[i] with nums[j]
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
}
