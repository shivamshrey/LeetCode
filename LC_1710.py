# 1710. Maximum Units on a Truck

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        result = 0
        boxTypes.sort(key=lambda boxType: boxType[1], reverse=True)
        
        for box, units in boxTypes:
            if truckSize > box:
                result += box * units
                truckSize -= box
            else:
                result += truckSize * units
                return result
        
        return result
        