# 1807. Evaluate the Bracket Pairs of a String
# https://leetcode.com/problems/evaluate-the-bracket-pairs-of-a-string/

class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        knowledge_dict = dict(knowledge)
        result = []
        i = 0
        while i < len(s):
            if s[i] == '(':
                j = i + 1
                while s[j] != ')':
                    j += 1
                
                result.append(knowledge_dict.get(s[i + 1:j], "?"))
                i = j
            else:
                result.append(s[i])
            i += 1
        
        return ''.join(result)
    