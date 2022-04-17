# 465. Optimal Account Balancing
# https://leetcode.com/problems/optimal-account-balancing/

class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        def backtrack(i):
            while i < len(debts) and debts[i] == 0:  # skip zero values
                i += 1
            if i == len(debts): return 0    # all settled
            
            result = float('inf')
            for j in range(i + 1, len(debts)):
                if debts[j] * debts[i] < 0:
                    # only if one value is positive and the
                    # other negative, can we possibly settle debts.
                    
                    # settle i with j
                    debts[j] += debts[i]
                    result = min(result, 1 + backtrack(i + 1))
                    # backtrack
                    debts[j] -= debts[i]
            return result
        
        balances = collections.defaultdict(int) # initial state for every person
        for transaction in transactions:
            balances[transaction[0]] -= transaction[2]
            balances[transaction[1]] += transaction[2]
        
        debts = [val for val in balances.values() if val != 0]  # only non-zero values
        return backtrack(0)
    