// 215. Kth Largest Element in an Array

// TC: O(n log k)
// SC: O(k)

class Solution {
    public int findKthLargest(int[] nums, int k) {
        Queue<Integer> minheap = new PriorityQueue<>();
        for (int num : nums) {
            minheap.offer(num);
            if (minheap.size() > k)
                minheap.poll();
        }
        return minheap.poll();
    }
}
