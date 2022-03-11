class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        def encode(word):
            char_counter = [0] * 26
            for ch in word:
                index = ord(ch) - ord('a')
                char_counter[index] += 1
            return tuple(char_counter)

        store = defaultdict(list)
        for word in strs:
            store[encode(word)].append(word)

        return store.values()
    
#         store = defaultdict(list)
#         for word in strs:
#             store[tuple(sorted(word))].append(word)

#         return store.values()