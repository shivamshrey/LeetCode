// 347. Top K Frequent Elements

class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> frequencies = new HashMap<>();
        for (int num : nums)
            frequencies.put(num, frequencies.getOrDefault(num, 0) + 1);
        
        // heap with the least frequent element first
        Queue<Integer> heap = new PriorityQueue<>(
            (num1, num2) -> frequencies.get(num1) - frequencies.get(num2));
        
        for (int num : frequencies.keySet()) {
            heap.offer(num);
            if (heap.size() > k)
                heap.poll();
        }
        
        return heap.stream().mapToInt(Integer::intValue).toArray();
    }
}
