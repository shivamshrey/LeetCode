# 2034. Stock Price Fluctuation
# https://leetcode.com/problems/stock-price-fluctuation/

class StockPrice:

    def __init__(self):
        self.minheap = []
        self.maxheap = []
        self.prices = dict()
        self.latest_timestamp = 0

    def update(self, timestamp: int, price: int) -> None:
        self.latest_timestamp = max(self.latest_timestamp, timestamp)
        self.prices[timestamp] = price
        
        heapq.heappush(self.minheap, (price, timestamp))
        heapq.heappush(self.maxheap, (-price, timestamp))

    def current(self) -> int:
        return self.prices[self.latest_timestamp]

    def maximum(self) -> int:
        while self.prices[self.maxheap[0][1]] != -self.maxheap[0][0]:
            heapq.heappop(self.maxheap)
        return -self.maxheap[0][0]

    def minimum(self) -> int:
        while self.prices[self.minheap[0][1]] != self.minheap[0][0]:
            heapq.heappop(self.minheap)
        return self.minheap[0][0]


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()