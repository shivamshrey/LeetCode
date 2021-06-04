# 17. Letter Combinations of a Phone Number

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        result = []
        
        mapping = ["0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        
        self.letterCombinationsUtil(digits, mapping, result, "", 0)
        return result
    
    def letterCombinationsUtil(self, digits, mapping, result, cur, index):
        if len(cur) == len(digits):
            result.append(cur)
            return
        
        letters = mapping[int(digits[index])]
        
        for i in range(len(letters)):
            self.letterCombinationsUtil(digits, mapping, result, cur + letters[i], index + 1)
        