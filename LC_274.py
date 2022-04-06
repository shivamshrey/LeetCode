# 274. H-Index
# https://leetcode.com/problems/h-index/

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        result = 0
        for i, citation in enumerate(citations):
            if i + 1 <= citation:
                result += 1
        return result