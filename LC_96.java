// 96. Unique Binary Search Trees

class Solution {
    public int numTrees(int n) {
        int[] catalanArr = new int[n + 1];
        catalanArr[0] = catalanArr[1] = 1;
        
        for (int i = 2; i <= n; i++)
            for (int j = 0; j < i; j++)
                catalanArr[i] += catalanArr[j] * catalanArr[i - j - 1];
        
        return catalanArr[n];
    }
}
