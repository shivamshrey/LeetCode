// 59. Spiral Matrix II

class Solution {
    public int[][] generateMatrix(int n) {
        int[][] matrix = new int[n][n];
        
        int top = 0, bottom = n - 1;
        int left = 0, right = n - 1;
        int direction = 0;  // initially, right
        int value = 1;
        while (top <= bottom && left <= right) {
            if (direction == 0) {   // right
                for (int j = left; j <= right; j++)
                    matrix[top][j] = value++;
                top++;
            } else if (direction == 1) {    // down
                for (int i = top; i <= bottom; i++)
                    matrix[i][right] = value++;
                right--;
            } else if (direction == 2) {    // left
                for (int j = right; j >= left; j--)
                    matrix[bottom][j] = value++;
                bottom--;
            } else {    // up
                for (int i = bottom; i >= top; i--)
                    matrix[i][left] = value++;
                left++;
            }
            direction = (direction + 1) % 4;
        }
        return matrix;
    }
}
