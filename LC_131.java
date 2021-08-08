// 131. Palindrome Partitioning

class Solution {
    public List<List<String>> partition(String s) {
        List<List<String>> result = new ArrayList<List<String>>();
        
        backtrack(s, 0, new ArrayList<String>(), result);
        return result;
    }
    
    public void backtrack(String s, int start, List<String> curList, List<List<String>> result) {
        if (start == s.length()) {
            result.add(new ArrayList<>(curList));
            return;
        }
        
        for (int end = start; end < s.length(); end++) {
            if (isPalindrome(s, start, end)) {
                curList.add(s.substring(start, end + 1));
                backtrack(s, end + 1, curList, result);
                curList.remove(curList.size() - 1);
            }
        }
    }
    
    public boolean isPalindrome(String s, int low, int high) {
        while (low < high) {
            if (s.charAt(low++) != s.charAt(high--))
                return false;
        }
        return true;
    }
}
