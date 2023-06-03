class Solution(object):
    def slowestKey(self, releaseTimes, keysPressed):
        """
        :type releaseTimes: List[int]
        :type keysPressed: str
        :rtype: str
        """
        releaseTimes = [0] + releaseTimes
        durations = [releaseTimes[i] - releaseTimes[i -1] for i in range(1, len(releaseTimes))]
        print(durations)
        max_so_far = float("-inf")
        output = ""
        
        for duration, ch in zip(durations, keysPressed):
            if duration > max_so_far:
                max_so_far = duration
                output = ch
            
            if duration == max_so_far:
                output = max(output, ch)
                
        return output