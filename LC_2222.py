# 2222. Number of Ways to Select Buildings
# https://leetcode.com/problems/number-of-ways-to-select-buildings/

# TC: O(n)
# SC: O(1)

class Solution:
    def numberOfWays(self, s: str) -> int:
        count0 = count1 = 0 # counts of '0' and '1' respectively
        for i in s:
            if i == '0': count0 += 1
            else: count1 += 1
        
        count0_so_far = count1_so_far = 0   # acts as counts of '0' and '1' to the left of current building respectively
        result = 0
    
        for i in s:
            if i == '0':    # count '101' pattern
                result += count1_so_far * (count1 - count1_so_far)
                count0_so_far += 1
            else:           # count '010' pattern
                result += count0_so_far * (count0 - count0_so_far)
                count1_so_far += 1
        
        return result
    