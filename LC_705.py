# 705. Design HashSet

class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # https://en.wikipedia.org/wiki/Hash_function#Multiplicative_hashing
        # We use separate chaining technique to handle collisions
        self.a = 1031237
        self.w = 20
        self.m = 15
        self.arr = [[] for _ in range(1 << self.m)]

    def _hash(self, key: int) -> int:
        # Trick: s % t = s & ((1 << t) - 1)
        # Using hash(K) = (aK mod 2^w) / 2^(w-m)
        return ((self.a * key) & ((1 << self.w) - 1)) >> (self.w - self.m)
    
    def add(self, key: int) -> None:
        i = self._hash(key)
        if key not in self.arr[i]:
            self.arr[i].append(key)

    def remove(self, key: int) -> None:
        i = self._hash(key)
        if key in self.arr[i]:
            self.arr[i].remove(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        i = self._hash(key)
        return key in self.arr[i]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
