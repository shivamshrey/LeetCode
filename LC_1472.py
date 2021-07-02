# 1472. Design Browser History

class BrowserHistory:

    def __init__(self, homepage: str):
        self.stack = [homepage]
        self.cur = 0

    def visit(self, url: str) -> None:
        # clear forward history if it exists
        ptr = len(self.stack) - 1
        while ptr > self.cur:
            self.stack.pop()
            ptr -= 1
        
        self.stack.append(url)
        self.cur += 1

    def back(self, steps: int) -> str:
        self.cur = max(0, self.cur - steps)
        return self.stack[self.cur]
    
    def forward(self, steps: int) -> str:
        self.cur = min(len(self.stack) - 1, self.cur + steps)
        return self.stack[self.cur]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
