# 1657. Determine if Two Strings Are Close
# https://leetcode.com/problems/determine-if-two-strings-are-close/

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        word1_counter, word2_counter = Counter(word1), Counter(word2)
        return word1_counter.keys() == word2_counter.keys() and Counter(word1_counter.values()) == Counter(word2_counter.values())
    