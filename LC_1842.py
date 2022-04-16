# 1842. Next Palindrome Using Same Digits
# https://leetcode.com/problems/next-palindrome-using-same-digits/

class Solution:
    def nextPalindrome(self, num: str) -> str:
        num = list(num)
        
        mid = len(num) >> 1
        if len(num) & 1: 
            mid_num = [num[mid]]
        else:
            mid_num = []
        
        first_half = num[:mid]
        next_permutation = self.nextPermutation(first_half)
        if not next_permutation:
            return ""
        return ''.join(next_permutation + mid_num + next_permutation[::-1])
        
    def nextPermutation(self, nums: List) -> List:    
        i = len(nums) - 2
        while i > -1:
            if nums[i] < nums[i + 1]:
                j = len(nums) - 1
                while j > i:
                    if nums[j] > nums[i]:
                        break
                    j -= 1
                nums[i], nums[j] = nums[j], nums[i]
                break
            i -= 1
        
        if i < 0: return None
        
        # reversing a non-increasing array is the same as sorting it
        nums[i + 1:] = reversed(nums[i + 1:])
        return nums
    