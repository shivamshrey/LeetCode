# 205. Isomorphic Strings

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hm1 = [-1] * 256
        hm2 = [-1] * 256
        
        for i in range(len(s)):
            if hm1[ord(s[i])] != hm2[ord(t[i])]:
                return False
            hm1[ord(s[i])] = hm2[ord(t[i])] = i
            
        return True
    