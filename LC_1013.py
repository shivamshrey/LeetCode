# 1013. Partition Array Into Three Parts With Equal Sum

class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        average_sum, remainder = divmod(sum(arr), 3)
        count = 0
        part_sum = 0
        
        for num in arr:
            part_sum += num
            if part_sum == average_sum:
                count += 1
                part_sum = 0
        
        return remainder == 0 and count >= 3
    