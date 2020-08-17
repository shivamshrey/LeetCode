class Solution {
    public int lengthOfLongestSubstring(String s) {
        int len = s.length();
        int max = 0;
        int i = 0, j = 0;
        
        boolean[] count = new boolean[255];
        
        while (j < len) {
            if (!count[s.charAt(j)]) {
                count[s.charAt(j)] = true;
                j++;
                max = Math.max(max, j - i);
            } else {
                count[s.charAt(i)] = false;
                i++;
            }
        }
        
        return max;
    }
}
