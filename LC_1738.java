// 1738. Find Kth Largest XOR Coordinate Value

class Solution {
    public int kthLargestValue(int[][] matrix, int k) {
        PriorityQueue<Integer> priorityQueue = new PriorityQueue<>();
        
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[0].length; j++) {
                if (i != 0) {
                    matrix[i][j] ^= matrix[i - 1][j];
                }
                if (j != 0) {
                    matrix[i][j] ^= matrix[i][j - 1];
                }
                if (i != 0 && j != 0) {
                    matrix[i][j] ^= matrix[i - 1][j - 1];
                }
                priorityQueue.add(matrix[i][j]);
                if (priorityQueue.size() > k) {
                    priorityQueue.poll();
                }
            }
        }
        
        return priorityQueue.poll();
    }
}
    