# 290. Word Pattern

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        if len(words) != len(pattern):
            return False
        
        pattern_to_word = dict()
        word_to_pattern = dict()
        
        for i in range(len(pattern)):
            if pattern[i] in pattern_to_word and pattern_to_word[pattern[i]] != words[i]:
                return False
            if words[i] in word_to_pattern and word_to_pattern[words[i]] != pattern[i]:
                return False
            pattern_to_word[pattern[i]] = words[i]
            word_to_pattern[words[i]] = pattern[i]
            
        return True
