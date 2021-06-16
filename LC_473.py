# 473. Matchsticks to Square

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        perimeter = sum(matchsticks)
        if perimeter % 4 != 0:
            return False
        possible_side = perimeter // 4
        
        # to store lengths of all 4 sides
        sides = [0] * 4
        
        # optimization: matchsticks of size bigger than possible_side
        # will be encountered early
        matchsticks.sort(reverse=True)
        # optimization: if the biggest matchstick > possible_side,
        # square can't be formed
        if matchsticks[0] > possible_side:
            return False
        
        def dfs(index):
            # when all matchsticks are consumed
            if index == len(matchsticks):
                return sides[0] == sides[1] == sides[2] == possible_side
            
            for i in range(4):
                if sides[i] + matchsticks[index] <= possible_side:
                    sides[i] += matchsticks[index]
                    if dfs(index + 1):
                        return True
                    sides[i] -= matchsticks[index]
            
            return False
        
        return dfs(0)
    