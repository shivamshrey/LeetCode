# 1696. Jump Game VI

class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        dp = [-float('inf')] * len(nums)
        dp[0] = nums[0]
        # each value in dq is a tuple (dp[i], i)
        dq = deque([(nums[0], 0)])
        
        for i in range(1, len(nums)):
            dp[i] = nums[i] + dq[0][0]
            
            # remove all smaller dp values from dq from right
            while dq and dq[-1][0] < dp[i]:
                dq.pop()
            # append the new dp value to dq
            dq.append((dp[i], i))
            
            # remove the max dp value from dq
            # if it doesn't fit in k-size window
            if i - k == dq[0][1]:
                dq.popleft()
            
        return dp[-1]
            