// 383. Ransom Note

class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        int[] frequencies = new int[26];
        for (int i = 0; i < magazine.length(); i++)
            frequencies[magazine.charAt(i) - 'a']++;
        
        for (int i = 0; i < ransomNote.length(); i++) {
            if (--frequencies[ransomNote.charAt(i) - 'a'] < 0)
                return false;
        }
        return true;
    }
}
