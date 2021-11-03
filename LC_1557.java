// 1557. Minimum Number of Vertices to Reach All Nodes

class Solution {
    public List<Integer> findSmallestSetOfVertices(int n, List<List<Integer>> edges) {
        Set<Integer> set = new HashSet<>(IntStream.range(0, n).boxed().collect(Collectors.toList()));
        
        for (List edge : edges)
            set.remove(edge.get(1));
        
        return new ArrayList(set);
    }
}
