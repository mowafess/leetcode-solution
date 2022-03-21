class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        stack = [0]
        visited = set([0])
        counter = 1
        
        while stack:
            key = stack.pop()
            others = rooms[key]
            
            for room in others:
                if room not in visited:
                    stack.append(room)
                    visited.add(room)
                    counter += 1
        
        return counter == len(rooms)
            
        
        
        
        