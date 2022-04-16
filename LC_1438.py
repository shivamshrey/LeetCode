# 1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
# https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/

# TC: O(n)
# SC: O(n)
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        increasing = collections.deque()    # gives maximum
        decreasing = collections.deque()    # gives minimum
        
        i = 0   # i..j is the window
        for j in range(len(nums)):
            while increasing and increasing[-1] > nums[j]: increasing.pop()
            increasing.append(nums[j])
            
            while decreasing and decreasing[-1] < nums[j]: decreasing.pop()
            decreasing.append(nums[j])
            
            if decreasing[0] - increasing[0] > limit:
                # The biggest difference is over the limit; so remove nums[i] from the window.
                # Why do we check only decreasing[0]/increasing[0] to remove nums[i]?
                # Take decreasing as an example. In order for nums[i] to be present in decreasing, 
                # nums[i] >= nums[x], where x = i+1...j. In other words, it has to be the biggest element or 
                # it would have already been removed. The biggest element would be in decreasing[0]. 
                # Similar explanation applies for increasing.
                if decreasing[0] == nums[i]: decreasing.popleft()
                if increasing[0] == nums[i]: increasing.popleft()
                i += 1
        
        # At every iteration of j, the window size for consideration is from A[i..j]. Its size is j+1-i.
        # At every iteration, an element is added to the window and possibly removed only if the window contains
        # elements with max difference > limit.
        # So the window size only grows monotonically but never shrinks in size. The window grows only if all the elements in
        # the window satisfy the max difference <= limit.
        # Therefore, the last window size in the iteration(when j=len(A)-1) holds the maximum size of the window with max diff <= limit.
        # However, it must be noted that the window in consideration at the last iteration may not really be the window
        # which has the max diff <= limit.
        # This doesn't matter since all we are interested in is the window size and not really the elements in the window.
        return len(nums) - i
