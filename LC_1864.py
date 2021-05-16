# 1864. Minimum Number of Swaps to Make the Binary String Alternating

class Solution:
    def minSwaps(self, s: str) -> int:
        n = len(s)
        zeros = 0   # count of 0s
        ones = 0    # count of 1s
        
        for c in s:
            if c == '0':
                zeros += 1
            else:
                ones += 1
                
        if abs(zeros - ones) > 1:   # impossible
            return -1
        
        if zeros > ones:        # alternating string should start with '0'
            return self.minSwapsUtil(s, '0')
        elif ones > zeros:      # alternating string should start with '1'
            return self.minSwapsUtil(s, '1')
        else:
            return min(self.minSwapsUtil(s, '0'), self.minSwapsUtil(s, '1')) 
        
    def minSwapsUtil(self, s: str, c: str) -> int:
        swaps = 0
        
        for char in s:
            if char != c:
                swaps += 1
            
            c = '1' if c == '0' else '0'
        
        return swaps // 2
    