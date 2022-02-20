class SnapshotArray:
    def __init__(self, length: int):
        self.snap_id = -1
        self.history = [[(self.snap_id, 0)] for _ in range(length)] # list of histories (snap_id, value)
        self.snap_id = 0
       

    def set(self, index: int, val: int) -> None:
        self.history[index].append((self.snap_id, val))
        

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

   
    def get(self, index: int, snap_id: int) -> int:
        history = self.history[index]
        lower = bisect.bisect(history, snap_id, key=lambda x: x[0])
        # lower, upper = 0, len(history) - 1
        # while lower != upper:
        #     mid = (upper + lower) // 2 + 1
        #     if history[mid][0] <= snap_id:
        #         lower = mid
        #     else: # history[mid][0] > snap_id implying history[mid-1][0] is >= snap_id - 1
        #         upper = mid - 1
            
        return history[lower-1][1]


# from collections import defaultdict
# class SnapshotArray:

#     def __init__(self, length: int):
#         self.length = length
#         self.id = 0
#         self.snapshots = defaultdict(dict)

#     def set(self, index: int, val: int) -> None:
#         self.snapshots[self.id][index] = val

#     def snap(self) -> int:
#         current_id = self.id
#         self.id += 1
#         return current_id

#     def get(self, index: int, snap_id: int) -> int:
#         while snap_id >=0:
#             if index in self.snapshots[snap_id]:
#                 return self.snapshots[snap_id][index]
#             snap_id -= 1
#         return 0

# class SnapshotArray:

#     def __init__(self, length: int):
#         self.curr = [0] * length
#         self.history = []
#         self.max_length = 0
        
#     def set(self, index: int, val: int) -> None:
#         self.curr[index] = val
#         self.max_length = max(self.max_length, index + 1)
        
#     def snap(self) -> int:
#         self.history.append(self.curr[:self.max_length])
#         return len(self.history) - 1

#     def get(self, index: int, snap_id: int) -> int:
#         return 0 if index > len(self.history[snap_id]) - 1 else self.history[snap_id][index]
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)