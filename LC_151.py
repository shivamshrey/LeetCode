# 151. Reverse Words in a String
# https://leetcode.com/problems/reverse-words-in-a-string/

class Solution:
    def reverseWords(self, s: str) -> str:
        words = re.split(" +", s.strip())
        words.reverse()
        return " ".join(words)
    