# 1220. Count Vowels Permutation
# https://leetcode.com/problems/count-vowels-permutation/

class Solution:
    def countVowelPermutation(self, n: int) -> int:
        a_count = e_count = i_count = o_count = u_count = 1
        MOD = 10 ** 9 + 7
        
        for j in range(1, n):
            a_count_new = (e_count + i_count + u_count) % MOD
            e_count_new = (a_count + i_count) % MOD
            i_count_new = (e_count + o_count) % MOD
            o_count_new = (i_count) % MOD
            u_count_new = (i_count + o_count) % MOD
            
            a_count, e_count, i_count, o_count, u_count = \
                a_count_new, e_count_new, i_count_new, o_count_new, u_count_new
        
        return (a_count + e_count + i_count + o_count + u_count) % MOD
    
    