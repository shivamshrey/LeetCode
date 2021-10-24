# 290. Word Pattern

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        if len(words) != len(pattern):
            return False
        
        pattern_to_word = dict()
        word_to_pattern = dict()
        
        for i in range(len(pattern)):
            if pattern_to_word.get(pattern[i], None) != word_to_pattern.get(words[i], None):
                return False
            pattern_to_word[pattern[i]] = i
            word_to_pattern[words[i]] = i
            
        return True
