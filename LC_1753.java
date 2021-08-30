// 1753. Maximum Score From Removing Stones

class Solution {
    public int maximumScore(int a, int b, int c) {
        PriorityQueue<Integer> priorityQueue = new PriorityQueue<>((n1, n2) -> n2 - n1);
        priorityQueue.add(a);
        priorityQueue.add(b);
        priorityQueue.add(c);
        int score = 0;
        
        while (true) {
            int x = priorityQueue.poll();
            int y = priorityQueue.poll();
            if (x == 0 || y == 0) 
                break;
            score++;
            priorityQueue.add(x - 1);
            priorityQueue.add(y - 1);
        }
        
        return score;
    }
}
