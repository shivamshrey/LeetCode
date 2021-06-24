# 560. Subarray Sum Equals K

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hm = {0: 1} # {cur_sum: no. of occurrences of cur_sum}
        count = 0
        
        cur_sum = 0
        for num in nums:
            cur_sum += num
            if cur_sum - k in hm:
                count += hm[cur_sum - k]
            hm[cur_sum] = hm.get(cur_sum, 0) + 1
        return count
