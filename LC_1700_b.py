# 1700. Number of Students Unable to Eat Lunch

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = collections.Counter(students)
        i = 0
        
        while i < len(sandwiches) and count[sandwiches[i]]:
            count[sandwiches[i]] -= 1
            i += 1
            
        return len(students) - i
    