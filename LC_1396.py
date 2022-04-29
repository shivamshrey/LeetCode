# 1396. Design Underground System
# https://leetcode.com/problems/design-underground-system/

class UndergroundSystem:

    def __init__(self):
        self.checkInHashmap = dict()    # stationName -> checkintime
        self.duration = collections.defaultdict(lambda : [0, 0])    # (source, destination) -> [totalTrip time across all trips, total number of trips]

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if id not in self.checkInHashmap:
            self.checkInHashmap[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, sourceTime = self.checkInHashmap.pop(id)
        self.duration[(startStation, stationName)][0] += t - sourceTime
        self.duration[(startStation, stationName)][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        totalTime, totalTrips = self.duration[(startStation, endStation)]
        return totalTime / totalTrips


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)