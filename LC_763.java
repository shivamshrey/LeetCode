// 763. Partition Labels

class Solution {
    public List<Integer> partitionLabels(String s) {
        List<Integer> result = new ArrayList<>();
        Map<Character, Integer> last = new HashMap<>();
        for (int i = 0; i < s.length(); i++)
            last.put(s.charAt(i), i);
        
        int j = 0, anchor = 0;
        
        for (int i = 0; i < s.length(); i++) {
            j = Math.max(j, last.get(s.charAt(i)));
            if (i == j) {
                result.add(i - anchor + 1);
                anchor = i + 1;
            }                
        }
        
        return result;
    }
}
