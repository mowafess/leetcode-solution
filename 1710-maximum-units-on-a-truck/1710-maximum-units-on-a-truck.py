class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes = sorted(boxTypes, key=lambda x: -x[1])
        
        i = result = 0
        
        while truckSize > 0 and i < len(boxTypes):
            num = min(boxTypes[i][0], truckSize)
            result += num * boxTypes[i][1]
            truckSize -= num
            i += 1
            
        return result
        