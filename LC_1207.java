class Solution {
    public boolean uniqueOccurrences(int[] arr) {
        Map<Integer, Integer> hashmap = new HashMap<>();
        Set<Integer> hashset = new HashSet<>();
        
        for (int i = 0; i < arr.length; i++)
            hashmap.put(arr[i], hashmap.getOrDefault(arr[i], 0) + 1);
        
        for (Map.Entry<Integer, Integer> entry : hashmap.entrySet())
            if (!hashset.add(entry.getValue()))
                return false;
        
        return true;
    }
}
