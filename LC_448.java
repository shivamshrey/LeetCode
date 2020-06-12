class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        
        List<Integer> missingNumbers = new ArrayList<>();
        int[] map = new int[nums.length];
        
        for (int i = 0; i < nums.length; i++)
            map[nums[i]-1] = 1;
            
        for (int i = 0; i < nums.length; i++)
            if (map[i] == 0)
                missingNumbers.add(i+1);
        
        return missingNumbers;
    }
}