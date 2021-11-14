// 40. Combination Sum II

class Solution {
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        List<List<Integer>> result = new ArrayList<>();
        Arrays.sort(candidates);
        backtrack(candidates, target, result, new ArrayList<>(), 0);
        return result;
    }
    
    private void backtrack(int[] candidates, int target, List<List<Integer>> result, List<Integer> combination, int start) {
        if (target == 0) {
            result.add(new ArrayList(combination));
            return;
        }
        
        for (int i = start; i < candidates.length; i++) {
            if (i > start && candidates[i] == candidates[i - 1]) continue; 
            if (target - candidates[i] >= 0) {
                combination.add(candidates[i]);
                backtrack(candidates, target - candidates[i], result, combination, i + 1);
                combination.remove(combination.size() - 1);
            }
        }
    }
}
