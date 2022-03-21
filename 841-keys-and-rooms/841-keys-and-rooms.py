class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        queue = [0]
        visited = set([0])
        counter = 1
        
        while queue:
            key = queue.pop()
            others = rooms[key]
            
            for room in others:
                if room not in visited:
                    queue.append(room)
                    visited.add(room)
                    counter += 1
        
        return counter == len(rooms)
            
        
        
        
        