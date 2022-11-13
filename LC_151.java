// 151. Reverse Words in a String
// https://leetcode.com/problems/reverse-words-in-a-string/

class Solution {
    public String reverseWords(String s) {
        String[] words = s.strip().split(" +");
        Collections.reverse(Arrays.asList(words));
        return String.join(" ", words);
    }
}
