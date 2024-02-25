class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        def encode(s):
            code = [0] * 26
            base = ord('a')
            for ch in s:
                code[ord(ch)-base] += 1
            
            return tuple(code)
        
        freq = collections.defaultdict(list)
        
        for s in strs:
            freq[encode(s)].append(s)
            
        return list(freq.values())
            