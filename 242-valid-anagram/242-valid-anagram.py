class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s) != len(t) or set(s) != set(t):
        #     return False
        
        # freqTable = defaultdict(int)

        # for i in range(len(s)):
        #     freqTable[s[i]] += 1
        #     freqTable[t[i]] -= 1

        # for k, v in freqTable.items():
        #     if v != 0:
        #         return False

        # return True

        if len(s) != len(t):
            return False  
        return (Counter(s) - Counter(t)) == Counter()