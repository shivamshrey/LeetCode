class Solution {
    public int heightChecker(int[] heights) {
        
        int count = 0;
        int[] heightsCopy = new int[heights.length];
        System.arraycopy(heights, 0, heightsCopy, 0, heights.length);
        
        Arrays.sort(heightsCopy);
        
        for (int i = 0; i < heights.length; i++)
            if (heightsCopy[i] != heights[i])
                count++;
        
        return count;
        
    }
}