# 905. Sort Array By Parity

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        even = 0
        odd = len(A) - 1
        
        while even < odd:
            while even < len(A) and A[even] & 1 == 0:
                even += 1
            while odd > -1 and A[odd] & 1:
                odd -= 1
            if even < odd:
                A[even], A[odd] = A[odd], A[even]
        
        return A
    