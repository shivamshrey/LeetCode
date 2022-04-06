# 923. 3Sum With Multiplicity
# https://leetcode.com/problems/3sum-with-multiplicity/

class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        counts, result = collections.Counter(arr), 0
        for i in counts:
            for j in counts:
                k = target - i - j
                if i == j == k:
                    result += counts[i] * (counts[i] - 1) * (counts[i] - 2) // 6
                elif i == j:
                    result += counts[i] * (counts[i] - 1) // 2 * counts[k]
                elif i < j < k:
                    result += counts[i] * counts[j] * counts[k]
        return result % (10**9 + 7)
