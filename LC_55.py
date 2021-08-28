# 55. Jump Game

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        
        for i, cur_max_jump in enumerate(nums):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + cur_max_jump)
        
        return True
        