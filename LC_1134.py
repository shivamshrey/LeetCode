# 1134. Armstrong Number

class Solution:
    def isArmstrong(self, n: int) -> bool:
        k = len(str(n))
        temp1 = n
        temp2 = 0
        
        while temp1 > 0:
            temp2 += (temp1 % 10) ** k
            temp1 //= 10
        
        return temp2 == n
        