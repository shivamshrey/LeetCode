# 622. Design Circular Queue

class MyCircularQueue:

    def __init__(self, k: int):
        self._size = 0
        self._front, self._rear = 0, 0
        self._capacity = k
        self._data = [-1] * k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self._data[self._rear] = value
        else:
            self._rear = (self._rear + 1) % self._capacity
            self._data[self._rear] = value
        self._size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self._data[self._front] = -1
        self._front = (self._front + 1) % self._capacity
        self._size -= 1
        if self.isEmpty():
            self._rear = self._front
        return True

    def Front(self) -> int:
        return self._data[self._front]

    def Rear(self) -> int:
        return self._data[self._rear]        

    def isEmpty(self) -> bool:
        return self._size == 0

    def isFull(self) -> bool:
        return self._size == self._capacity


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
