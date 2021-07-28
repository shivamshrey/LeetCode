# 1670. Design Front Middle Back Queue

class FrontMiddleBackQueue:

    def __init__(self):
        self.queue = collections.deque()

    def pushFront(self, val: int) -> None:
        self.queue.appendleft(val)

    def pushMiddle(self, val: int) -> None:
        self.queue.insert(len(self.queue) // 2, val)

    def pushBack(self, val: int) -> None:
        self.queue.append(val)

    def popFront(self) -> int:
        return self.queue.popleft() if self.queue else -1

    def popMiddle(self) -> int:
        if not self.queue:
            return -1
    
        mid = (len(self.queue) - 1) // 2
        val = self.queue[mid]
        del self.queue[mid]
        
        return val

    def popBack(self) -> int:
        return self.queue.pop() if self.queue else -1

# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()
