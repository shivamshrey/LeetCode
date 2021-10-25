// 5. Longest Palindromic Substring

// TC: O(n^2)
// SC: O(1)
class Solution {
    public String longestPalindrome(String s) {
        if (s.length() < 1)
            return "";
        
        int start = 0, end = 0;
        
        for (int i = 0; i < s.length(); i++) {
            int length1 = expandAroundCenter(s, i, i);      // center != ""
            int length2 = expandAroundCenter(s, i, i + 1);  // center = ""
            int maxLength = Math.max(length1, length2);
            
            if (maxLength > end - start) {
                start = i - (maxLength - 1) / 2;
                end = i + maxLength / 2;
            }
        }
        
        return s.substring(start, end + 1);
        
    }
    
    public int expandAroundCenter(String s, int left, int right) {
        while (left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)) {
            left--;
            right++;
        }
        
        return right - left - 1;
    }
}
