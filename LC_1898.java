// 1898. Maximum Number of Removable Characters
// https://leetcode.com/problems/maximum-number-of-removable-characters/

class Solution {
    public int maximumRemovals(String s, String p, int[] removable) {
        char[] letters = s.toCharArray();
        
        // Do binary search to find the max K value
        // 0 <= K <= removable.length
        int low = 0, high = removable.length;
        
        while (low <= high) {
            // 'mid' represents how many letters are removed in this round.
            int mid = low + (high - low) / 2;
            
            // 'Remove' those letters! 
            for (int i = 0; i < mid; i++) 
                letters[removable[i]] = '#';
            
            if (isSubsequence(p, letters))
                low = mid + 1;
            else {
                // Otherwise, replace back all the letters that were removed.
                // Then, change the upper boundary.
                for (int i = 0; i < mid; i++)
                    letters[removable[i]] = s.charAt(removable[i]);
                high = mid - 1;
            }
        }
        return high;
    }
    
    private boolean isSubsequence(String p, char[] letters) {
        int j = 0, i = 0;
        while (i < p.length() && j < letters.length) {
            if (p.charAt(i) == letters[j]) i++;
            j++;
        }
        
        return i == p.length();
    }
}
