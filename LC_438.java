// 438. Find All Anagrams in a String

class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        List<Integer> result = new ArrayList<>();
        int[] counts = new int[26];
        for (char c : p.toCharArray())
            counts[c - 'a']++;
        
        int start = 0, end = 0;
        
        while (end < s.length()) {
            // valid anagram
            if (counts[s.charAt(end) - 'a'] > 0) {
                counts[s.charAt(end) - 'a']--;
                end++;
                // window size becomes equal tp p.length()
                if (end - start == p.length())
                    result.add(start);
            } else if (start == end) {
                start++;
                end++;
            } else {
                counts[s.charAt(start) - 'a']++;
                start++;
            }
        }
        
        return result;
    }
}
