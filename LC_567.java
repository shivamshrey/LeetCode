// 567. Permutation in String

class Solution {
    public boolean checkInclusion(String s1, String s2) {
        int[] counts = new int[26];
        for (char c : s1.toCharArray())
            counts[c - 'a']++;
        
        int start = 0, end = 0;
        
        while (end < s2.length()) {
            // valid anagram
            if (counts[s2.charAt(end) - 'a'] > 0) {
                counts[s2.charAt(end) - 'a']--;
                end++;
                // window size becomes equal to s1.length()
                if (end - start == s1.length())
                    return true;
            } else if (start == end) {
                start++;
                end++;
            } else {
                counts[s2.charAt(start) - 'a']++;
                start++;
            }
        }
        
        return false;
    }
}
