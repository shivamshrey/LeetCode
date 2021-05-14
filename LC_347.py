# 347. Top K Frequent Elements

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # hashmap to store frequency of each number
        hm = dict()
        for i in range(len(nums)):
            hm[nums[i]] = hm.get(nums[i], 0) + 1
        
        # Store hm in heap as tuples (freq, num)
        heap = [(freq, num) for num, freq in hm.items()]

        # Get the k most frequent elements as (freq, num) pairs
        k_most_frequent = heapq.nlargest(k, heap)
        
        # Extract num from (freq, num) pairs
        result = [item[1] for item in k_most_frequent]
        
        return result
    