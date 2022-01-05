class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes = sorted(boxTypes, key=lambda x: -x[1])
        box = sum(box[0] for box in boxTypes)
        unit = sum(box[0] * box[1] for box in boxTypes)
        
        i = result = 0
        
        if truckSize > box:
            result, truckSize = divmod(box, truckSize)
            result *= unit
        
        while truckSize > 0:
            num = min(boxTypes[i][0], truckSize)
            result += num * boxTypes[i][1]
            truckSize -= num
            i += 1
        
            
        return result
        