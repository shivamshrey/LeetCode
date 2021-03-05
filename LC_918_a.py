# 918. Maximum Sum Circular Subarray

class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        normal_max_sum = self.maxSubarray(A)
        if normal_max_sum < 0:
            return normal_max_sum
        
        arr_sum = 0
        for i in range(len(A)):
            arr_sum += A[i]
            A[i] = -A[i]
        
        circular_max_sum = arr_sum + self.maxSubarray(A)
        
        return max(circular_max_sum, normal_max_sum)
        
    def maxSubarray(self, A: List[int]) -> int:
        cur_max = A[0]
        max_so_far = A[0]
        
        for i in range(1, len(A)):
            cur_max = max(cur_max + A[i], A[i])
            max_so_far = max(cur_max, max_so_far)
        
        return max_so_far
