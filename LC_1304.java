class Solution {
    public int[] sumZero(int n) {
        int[] result = new int[n];
        
        for (int i = 1, j = 0; i <= n / 2; i++) {
            result[j++] = i;
            result[j++] = i * (-1);
        }
        
        return result;
    }
}
