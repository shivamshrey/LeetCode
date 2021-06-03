# 1160. Find Words That Can Be Formed by Characters

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        result = 0
        chars_freq = [0] * 26
        for char in chars:
            chars_freq[ord(char) - ord('a')] += 1
        
        for word in words:
            chars_freq_copy = deepcopy(chars_freq)
            is_good = True
            
            for ch in word:
                chars_freq_copy[ord(ch) - ord('a')] -= 1
                if chars_freq_copy[ord(ch) - ord('a')] < 0:
                    is_good = False
                    break
            
            if is_good:
                result += len(word)
                
        return result
    