// 706. Design HashMap

class MyHashMap {
    
    class Entry {
        
        int key;
        int value;
        
        Entry(int key, int value) {
            this.key = key;
            this.value = value;
        }
    }
    
    final int SIZE = 769;
    List<Entry>[] hashmap;  // Array of LinkedList of Entries
    
    public MyHashMap() {
        hashmap = new LinkedList[SIZE];
    }
    
    private int hash(int key) {
        return Integer.hashCode(key) % SIZE;
    }
    
    public void put(int key, int value) {
        int index = hash(key);
        List<Entry> entries = hashmap[index];
        
        if (entries == null) {              // if no List exists at hashmap[index]
            hashmap[index] = new LinkedList<Entry>();
            hashmap[index].add(new Entry(key, value));
        } else {
            // Entry entry
            for (Entry entry : entries) {   
                if (entry.key == key) {     // if key exists
                    entry.value = value;
                    return;
                }
            }
            hashmap[index].add(new Entry(key, value));  // if key doesn't exist
        }        
    }
    
    public int get(int key) {
        int index = hash(key);
        List<Entry> entries = hashmap[index];
        
        if (entries == null) return -1;     // if no List exists at hashmap[index]
        
        for (Entry entry : entries) {
            if (entry.key == key)
                return entry.value;
        }
        
        return -1;
    }
    
    public void remove(int key) {
        int index = hash(key);
        List<Entry> entries = hashmap[index];
        
        if (entries == null) return;    // if no List exists at hashmap[index]
        
        for (Entry entry : entries) {
            if (entry.key == key) {     // remove entry if key exists
                entries.remove(entry);
                return;
            }
        }
    }
    
}

/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap obj = new MyHashMap();
 * obj.put(key,value);
 * int param_2 = obj.get(key);
 * obj.remove(key);
 */
