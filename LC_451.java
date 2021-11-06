// 451. Sort Characters By Frequency

class Solution {
    public String frequencySort(String s) {
        Map<Character, Integer> frequencies = new HashMap<>();
        for (Character c : s.toCharArray())
            frequencies.put(c, frequencies.getOrDefault(c, 0) + 1);
        
        Queue<Map.Entry<Character, Integer>> maxheap =
            new PriorityQueue<>((a, b) -> b.getValue() - a.getValue());
        maxheap.addAll(frequencies.entrySet());
        
        StringBuilder sb = new StringBuilder();
        while (maxheap.size() > 0) {
            Map.Entry<Character, Integer> entry = maxheap.poll();
            for (int i = 0; i < entry.getValue(); i++)
                sb.append(entry.getKey());
        }
        
        return sb.toString();
    }
}
