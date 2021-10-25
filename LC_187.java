// 187. Repeated DNA Sequences

class Solution {
    public List<String> findRepeatedDnaSequences(String s) {
        Set<String> seen = new HashSet<>();
        Set<String> repeated = new HashSet<>();
        
        for (int i = 0; i + 9 < s.length(); i++) {
            String sequence = s.substring(i, i + 10);
            if (!seen.add(sequence))
                repeated.add(sequence);
        }
        
        return new ArrayList(repeated);
    }
}
