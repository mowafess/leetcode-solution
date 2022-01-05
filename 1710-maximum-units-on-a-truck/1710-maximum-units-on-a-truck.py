# class Solution:
#     def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
#         boxTypes = sorted(boxTypes, key=lambda x: -x[1])
# #         box = sum(box[0] for box in boxTypes)
# #         unit = sum(box[0] * box[1] for box in boxTypes)
        
#         i = result = 0
        
#         # if truckSize > box:
#         #     result, truckSize = divmod(box, truckSize)
#         #     result *= unit
        
#         while truckSize > 0:
#             num = min(boxTypes[i][0], truckSize)
#             result += num * boxTypes[i][1]
#             truckSize -= num
#             i += 1
        
            
#         return result

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: -x[1])
        cur_size = 0
        max_units = 0
        for num_box, unit in boxTypes:
            max_units += unit * min(truckSize - cur_size, num_box)
            cur_size += min(truckSize - cur_size, num_box)
        return max_units