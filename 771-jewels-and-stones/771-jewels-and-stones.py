class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freq = Counter(stones)
        total = 0
        
        for jewel in jewels:
            total += freq[jewel]
        
        return total
        