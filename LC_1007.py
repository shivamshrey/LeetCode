# 1007. Minimum Domino Rotations For Equal Row
# https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        tops_counts = [0] * 7   # tops_counts[i] = occurrence of i in tops
        bottoms_counts = [0] * 7    # bottoms_counts[i] = occurrence of i in bottoms
        same = [0] * 7  # same[i] = occurrence of k, where k == A[i] == B[i]
        
        for i in range(len(tops)):
            tops_counts[tops[i]] += 1
            bottoms_counts[bottoms[i]] += 1
            if tops[i] == bottoms[i]:
                same[tops[i]] += 1
        
        for i in range(1, 7):
            if tops_counts[i] + bottoms_counts[i] - same[i] >= len(tops):
                return min(tops_counts[i], bottoms_counts[i]) - same[i]
        
        return -1
    