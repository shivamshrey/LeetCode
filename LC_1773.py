# 1773. Count Items Matching a Rule

class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        rule_key = {"type": 0, "color": 1, "name": 2}
        
        count = 0
        for item in items:
            if item[rule_key[ruleKey]] == ruleValue:
                count += 1
        
        return count
    