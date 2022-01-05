class Solution:
    
    """
    recursion only - brute force: t - O(2^N) - tree size, S - O(N)
    recursion with memoization: T - O(n) - max tree size, S - O(n) - depth of recursion tree
    
    """
    @lru_cache()
    def climbStairs(self, n: int) -> int:
        
#         if n < 1:
#             return 0
        
#         if n == 1 or n == 2 or n == 3:
#             return n
        
#         return self.climbStairs(n - 1) + self.climbStairs(n -2)

        
        
#         """
#         dp approach: this problem can be broken into subproblems, and it      
#         contains the optimal substructure property i.e. its optimal solution 
#         can be constructed efficiently from optimal solutions of its 
#         subproblems, we can use dynamic programming to solve this problem.

#         T - O(N) - single loop
#         S - O(N) - size of dp array
#         """
#         if n == 1:
#             return 1
#         dp = [0] * (n + 1)
#         dp[1] = 1
#         dp[2] = 2

#         for i in range(3, n + 1):
#             dp[i] = dp[i-1] + dp[i-2]

#         return dp[n]
    
    
#         """
#         Fibonacci Number
#         T - O(N) - single loop
#         S - O(1) 
        
        # """
        if n == 1:
            return 1
        
        first = 1
        second = 2

        for i in range(3, n + 1):
            first, second = second, first + second

        return second