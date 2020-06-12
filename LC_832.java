class Solution {
    public int[][] flipAndInvertImage(int[][] A) {
        
        for (int i = 0; i < A.length; i++) {
            A[i] = reverseArray(A[i]);
            for (int j = 0; j < A[i].length; j++)
                A[i][j] ^= 1;
        }
        
        return A;
    }
    
    public int[] reverseArray(int[] A) {
        
        for (int i = 0; i < A.length / 2; i++) {
            int temp = A[i];
            A[i] = A[A.length - 1 - i];
            A[A.length - 1 - i] = temp;
        }
        
        return A;
    }
}