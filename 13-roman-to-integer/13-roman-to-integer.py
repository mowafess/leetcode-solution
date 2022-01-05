class Solution:
    def romanToInt(self, s: str) -> int:
        
        symbols = {"I": 1, "V": 5, "X": 10, 
                   "L": 50, "C": 100, "D": 500,
                   "M": 1000}
        
        prev = curr = total = 0
        
        for ch in s:
            prev, curr = curr, symbols[ch]
            if curr <= prev:
                total += curr
            else:
                total += curr - 2 * prev
        
        return total
        
        