# 1700. Number of Students Unable to Eat Lunch

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        queue = deque(students)
        i = 0
        count = 0
        
        while queue and i < len(sandwiches):
            if queue[0] == sandwiches[i]:
                queue.popleft()
                i += 1
                count = 0
            else:
                queue.append(queue.popleft())
                count += 1
                if count == len(queue):
                    return count
        
        return 0
    