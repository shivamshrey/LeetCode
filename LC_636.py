# 636. Exclusive Time of Functions

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []
        result = [0] * n
        prev_time = 0
        
        for log in logs:
            f_id, typ, timestamp = log.split(':')
            f_id, timestamp = int(f_id), int(timestamp)
            
            if typ == 'start':
                if stack:
                    result[stack[-1]] += timestamp - prev_time
                stack.append(f_id)
                prev_time = timestamp
            else:
                result[stack.pop()] += timestamp - prev_time + 1
                prev_time = timestamp + 1
                
        return result
    