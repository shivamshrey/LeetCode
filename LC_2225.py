# 2225. Find Players With Zero or One Losses
# https://leetcode.com/problems/find-players-with-zero-or-one-losses/

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        lost = {}
        people = set()
        for i, j in matches:
            people.add(i)
            people.add(j)
        for i in people:
            lost[i] = 0
        for i, j in matches:
            lost[j] += 1
        zero = []
        one = []
        for i in people:
            if lost[i] == 0:
                zero.append(i)
            elif lost[i] == 1:
                one.append(i)
        zero.sort()
        one.sort()
        return [zero, one]
        