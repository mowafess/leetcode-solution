class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        output = [0] * len(seats)
        prev = -len(seats)
        
        for i in range(len(seats)):
            if not seats[i]:
                output[i] = i - prev
            else:
                prev = i
        print(output)
        
        prev = 0
        
        for i in reversed(range(len(seats))):
            if not seats[i]:
                output[i] = min(abs(prev - i), output[i])
            else:
                prev = i
        print(output)
        
        return max(output)
        