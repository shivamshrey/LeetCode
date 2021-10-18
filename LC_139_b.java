// 139. Word Break

// TC: O(n^3)
// SC: O(n)

class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {
        Set<String> wordDictSet = new HashSet<>(wordDict);
        // dp[i] = true if substring[0...i] is breakable
        boolean[] dp = new boolean[s.length() + 1];
        dp[0] = true;
        
        for (int end = 1; end <= s.length(); end++) {
            for (int start = 0; start < end; start++) {
                if (dp[start] && wordDictSet.contains(s.substring(start, end))) {
                    dp[end] = true;
                    break;
                }
            }
        }
        
        return dp[s.length()];
    }
}
