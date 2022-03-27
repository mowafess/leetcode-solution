class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # BFS: T-O(N.N.M), S-O(N)
        words = {(len(word), word) for word in wordDict}
        q = deque()
        visited = set()
        limit = len(s)
        
        q.append(0)
        
        while q:
            start = q.popleft()
            if start not in visited:
                for size, word in words:
                    end = start + size
                    if s[start:end] == word:
                        q.append(end)
                        if end == limit:
                            return True
                visited.add(start)
        
        return False
    
        # DP T - O(N * M)
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True
        
        for i in reversed(range(len(s))):
            for word in wordDict:
                if (i + len(word)) <= len(s) and s[i:i+len(word)] == word:
                    dp[i] = dp[i + len(word)]
                if dp[i]:
                    break
                    
        return dp[0]
        
        