# 1383. Maximum Performance of a Team

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        current_team = []
        max_team_performance = 0
        team_speed = 0
        
        # sort the engineers in decreasing order based on their efficiency.
        # this ensures the new_hire will have the minimum efficiency
        for new_hire_efficiency, new_hire_speed in sorted(zip(efficiency, speed), reverse=True):
            # if team is full, fire the slowest guy and update team_speed
            if len(current_team) == k:
                slow_guy_speed = heappop(current_team)
                team_speed -= slow_guy_speed
            
            # hire the new guy and update team_speed
            heappush(current_team, new_hire_speed)
            team_speed += new_hire_speed

            # calculate team performance with new guy and 
            # update max_team_performance if necessary
            performance_with_new_hire = team_speed * new_hire_efficiency
            max_team_performance = max(max_team_performance, performance_with_new_hire)
            
        return max_team_performance % 1000000007
        