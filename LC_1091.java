// 1091. Shortest Path in Binary Matrix

class Solution {
    public int shortestPathBinaryMatrix(int[][] grid) {
        if (grid == null || grid.length == 0 || grid[0][0] != 0)
            return -1;
        
        int[][] dirs = new int[][] {
            {-1, 0}, {1, 0}, {0, -1}, {0, 1},
            {-1, -1}, {-1, 1}, {1, -1}, {1, 1}
        };
        
        Queue<int[]> queue = new LinkedList<>();
        queue.offer(new int[] {0, 0, 0});
        
        while (!queue.isEmpty()) {
            int[] cur = queue.poll();
            if (cur[0] == grid.length - 1 && cur[1] == grid[0].length - 1)
                return cur[2] + 1;
            
            for (int[] dir : dirs) {
                int i = cur[0] + dir[0];
                int j = cur[1] + dir[1];
                
                if (i < 0 || i >= grid.length || j < 0 || j >= grid[0].length
                        || grid[i][j] != 0)
                    continue;
                
                grid[i][j] = 2;
                queue.offer(new int[] {i, j, cur[2] + 1});
            }
        }
        
        return -1;
    }
    
}
