// 841. Keys and Rooms

class Solution {
    public boolean canVisitAllRooms(List<List<Integer>> rooms) {
        boolean[] visited = new boolean[rooms.size()];
        dfs(rooms, visited, 0);
        for(int i = 0 ; i < visited.length ;  i++){
            if(!visited[i])
                return false;
        }
        return true;
    }
    
    public void dfs(List<List<Integer>> rooms, boolean[] visited, int room){
        if(visited[room]){
            return;
        }
        visited[room] = true;
        
        for(Integer keyForRooms: rooms.get(room)){
             dfs(rooms, visited, keyForRooms);
        }
    }
}
