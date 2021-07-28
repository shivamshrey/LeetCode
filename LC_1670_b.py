# 1670. Design Front Middle Back Queue

class FrontMiddleBackQueue:

    def __init__(self):
        self.q1 = collections.deque()
        self.q2 = collections.deque()

    def pushFront(self, val: int) -> None:
        self.q1.appendleft(val)
        self.balance()
        
    def pushMiddle(self, val: int) -> None:
        if len(self.q1) > len(self.q2):
            self.q2.appendleft(self.q1.pop())
        self.q1.append(val)

    def pushBack(self, val: int) -> None:
        self.q2.append(val)
        self.balance()

    def popFront(self) -> int:
        val = self.q1.popleft() if self.q1 else -1
        self.balance()
        return val

    def popMiddle(self) -> int:
        val = (self.q1 or [-1]).pop()
        self.balance()
        return val

    def popBack(self) -> int:
        val = (self.q2 or self.q1 or [-1]).pop()
        self.balance()
        return val
    
    def balance(self) -> None:
        # Keep len(self.q1) >= len(self.q2)
        if len(self.q1) > len(self.q2) + 1:
            self.q2.appendleft(self.q1.pop())
        if len(self.q1) < len(self.q2):
            self.q1.append(self.q2.popleft())

# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()
