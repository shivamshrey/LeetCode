// 739. Daily Temperatures

class Solution {
    public int[] dailyTemperatures(int[] T) {
        int[] result = new int[T.length];
        
        for (int i =T.length - 1; i > 0; i--)
            for (int j = i - 1; j >=0 && T[j] < T[i]; j--)
                result[j] = i - j;
        
        return result;
    }
}
