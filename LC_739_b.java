// 739. Daily Temperatures

class Solution {
    public int[] dailyTemperatures(int[] T) {
        int[] result = new int[T.length];
        Stack<Integer> nextGreatest = new Stack<>();
        
        for (int i = T.length - 1; i >= 0; i--) {
            while (!nextGreatest.empty() && T[i] >= T[nextGreatest.peek()])
                nextGreatest.pop();
            
            if (!nextGreatest.empty())
                result[i] = nextGreatest.peek() - i;
            
            nextGreatest.push(i);
        }
        
        return result;
    }
}
