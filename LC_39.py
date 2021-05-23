# 39. Combination Sum

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        temp = []
        ans = []
        candidates.sort()
        self.combinationSumUtil(candidates, temp, ans, target, 0)
        return ans
        
    def combinationSumUtil(self, candidates, temp, ans, target, index):
        if target == 0:
            ans.append(list(temp))
            return
        
        for i in range(index, len(candidates)):
            if target - candidates[i] >= 0:
                temp.append(candidates[i])
                self.combinationSumUtil(candidates, temp, ans, target - candidates[i], i)
                temp.remove(candidates[i])
                