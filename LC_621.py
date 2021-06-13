# 621. Task Scheduler

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        frequencies = Counter(tasks)
        frequencies = [value for key, value in frequencies.items()]
        max_frequency = max(frequencies)
        num_of_max_frequency_tasks = frequencies.count(max_frequency)
        
        return max(len(tasks), (max_frequency - 1) * (n + 1) + num_of_max_frequency_tasks)
        