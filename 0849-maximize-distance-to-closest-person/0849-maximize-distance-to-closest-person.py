class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        
        first_index = seats.index(1)
        last_index = seats[::-1].index(1)
        
        max_dist = max(first_index, last_index)
        
        for i in range(first_index + 1, len(seats)):
            if seats[i]:
                dist = (i - first_index) // 2
                max_dist = max(max_dist, dist)
                first_index = i
        
        return max_dist
        
        
        output = [0] * len(seats)
        prev = -len(seats) #or first index of 1
        
        
        for i in range(len(seats)):
            if not seats[i]:
                output[i] = i - prev
            else:
                prev = i

        for i in reversed(range(len(seats))):
            if not seats[i]:
                output[i] = min(abs(i - prev), output[i])
            else:
                prev = i
                
        return max(output)
        