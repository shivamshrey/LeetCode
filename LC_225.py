# 225. Implement Stack using Queues

class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = deque()
    
    # TC: O(n)
    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue.append(x)
        n = len(self.queue)
        for i in range(n - 1):
            self.queue.append(self.queue.popleft())

    # TC: O(1)
    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.queue.popleft()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.queue[0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not self.queue


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
