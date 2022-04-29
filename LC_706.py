# 706. Design HashMap
# https://leetcode.com/problems/design-hashmap/

class Bucket:
    
    def __init__(self):
        self.bucket = []

    def get(self, key):
        for k, v in self.bucket:
            if k == key:
                return v
        return -1

    def put(self, key, value):
        found = False
        for i, (k, v) in enumerate(self.bucket):
            if key == k:
                self.bucket[i] = (key, value)
                found = True
                break
        if not found:
            self.bucket.append((key, value))

    def remove(self, key):
        for i, (k, v) in enumerate(self.bucket):
            if key == k:
                del self.bucket[i]
        
class MyHashMap:
    
    def __init__(self):
        self.size = 769
        self.hashmap = [Bucket()] * self.size

    def put(self, key: int, value: int) -> None:
        index = key % self.size
        self.hashmap[index].put(key, value)         

    def get(self, key: int) -> int:
        index = key % self.size
        return self.hashmap[index].get(key)

    def remove(self, key: int) -> None:
        index = key % self.size
        self.hashmap[index].remove(key)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)