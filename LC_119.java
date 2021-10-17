// 119. Pascal's Triangle II

class Solution {
    public List<Integer> getRow(int rowIndex) {
        List<List<Integer>> result = new ArrayList<>();
        result.add(List.of(1));
        
        for (int i = 1; i <= rowIndex; i++) {
            List<Integer> prevRow = result.get(result.size() - 1);
            List<Integer> newRow = new ArrayList<>();
            
            newRow.add(1);
            
            for (int j = 1; j < i; j++)
                newRow.add(prevRow.get(j - 1) + prevRow.get(j));
            
            newRow.add(1);
            result.add(newRow);
        }
        
        return result.get(result.size() - 1);
    }
}
