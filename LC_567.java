// 567. Permutation in String

class Solution {
    public boolean checkInclusion(String s1, String s2) {
        int s1Len = s1.length();
        int s2Len = s2.length();
        for (int i = 0; i < s2Len - s1Len + 1; i++)
            if (areAnagrams(s1, s2.substring(i, i + s1Len)))
                return true;
        return false;
    }
    
    public boolean areAnagrams(String s1, String s2) {
        int[] count = new int[26];
        
        for (int i = 0; i < s1.length(); i++) {
            count[s1.charAt(i) - 'a']++;
            count[s2.charAt(i) - 'a']--;
        }
        
        for (int i = 0; i < 26; i++) {
            if (count[i] != 0)
                return false;
        }
        return true;
    }
}
