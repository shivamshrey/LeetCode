// 207. Course Schedule

class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        List<Integer>[] graph = new ArrayList[numCourses];
        int[] inDegrees = new int[numCourses];
        
        for (int i = 0; i < numCourses; i++)
            graph[i] = new ArrayList<>();
        
        for (int[] edge : prerequisites) {
            graph[edge[1]].add(edge[0]);
            inDegrees[edge[0]]++;
        }
        
        Queue<Integer> queue = new ArrayDeque<Integer>();
        
        for (int i = 0; i < numCourses; i++) {
            if (inDegrees[i] == 0)
                queue.offer(i);
        }
        
        int count = 0;
        
        while (!queue.isEmpty()) {
            int u = queue.poll();
            count++;
            
            for (Integer v : graph[u]) {
                if (--inDegrees[v] == 0) {
                    queue.offer(v);
                }
            }
        }
        
        return count == numCourses;
    }
}
