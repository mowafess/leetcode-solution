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

        for i in reversed(range(len(seats))):
            if not seats[i]:
                output[i] = min(abs(i - prev), output[i])
            else:
                prev = i
                
        return max(output)
        