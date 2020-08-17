class Solution {
    public int countNegatives(int[][] grid) {
        int maxIndex = grid[0].length;
        int result = 0;
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < maxIndex; j++) {
                if (grid[i][j] < 0) {
                    result += (maxIndex - j) * (grid.length - i);
                    maxIndex = j;
                }
            }
        }
        return result;
    }
}
