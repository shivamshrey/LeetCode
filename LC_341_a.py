# 341. Flatten Nested List Iterator

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    # TC: O(n + l)
    # n = no. of integers
    # l = no. of lists
    # SC: O(n) for result list
    def __init__(self, nestedList: [NestedInteger]):
        self.result = []
        self.flatten(nestedList)
        self.i = 0
    
    # TC: O(1)
    def next(self) -> int:
        if self.hasNext():
            value = self.result[self.i]
            self.i += 1
            return value
    
    # TC: O(1)
    def hasNext(self) -> bool:
        return self.i < len(self.result)
    
    # TC: O(n + l)
    # n = no. of integers
    # l = no. of lists
    # SC: O(d) for recursion
    def flatten(self, nestedList):
        for i in nestedList:
            if i.isInteger():
                self.result.append(i.getInteger())
            else:
                self.flatten(i.getList())

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
