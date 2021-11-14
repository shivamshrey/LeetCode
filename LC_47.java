// 47. Permutations II

class Solution {
    public List<List<Integer>> permuteUnique(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        Map<Integer, Integer> counts = new HashMap<>();
        
        for (int num : nums)
            counts.put(num, counts.getOrDefault(num, 0) + 1);
        
        backtrack(nums, result, new ArrayList(), counts);
        return result;
    }
    
    private void backtrack(int[] nums, List<List<Integer>> result, List<Integer> permutation, Map<Integer, Integer> counts) {
        if (permutation.size() == nums.length) {
            result.add(new ArrayList(permutation));
            return;
        }
        
        for (Map.Entry<Integer, Integer> e : counts.entrySet()) {
            if (e.getValue() > 0) {
                // add this number into the current combination
                permutation.add(e.getKey());
                counts.put(e.getKey(), e.getValue() - 1);
                
                // continue the exploration
                backtrack(nums, result, permutation, counts);
                
                // revert the choice for the next exploration
                permutation.remove(permutation.size() - 1);
                counts.put(e.getKey(), e.getValue() + 1);
            }
        }
    }
}
