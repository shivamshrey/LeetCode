class Solution {
    public int[] sortedSquares(int[] A) {
        
        int[] result = new int[A.length];
        
        int left = 0, right = A.length - 1, pos = A.length - 1;
        
        while (pos >= 0) {
            int leftCandidate = A[left] * A[left];
            int rightCandidate = A[right] * A[right];
            
            if (leftCandidate > rightCandidate) {
                result[pos] = leftCandidate;
                left++;
            }
            else {
                result[pos] = rightCandidate;
                right--;
            }
            pos--;
        }
        
        return result;
    }
}