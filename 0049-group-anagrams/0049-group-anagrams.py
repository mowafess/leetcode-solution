class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
#         groups = collections.defaultdict(list)
        
#         for word in strs:
#             groups[tuple(sorted(word))].append(word)
        
#         return list(groups.values())

        def encode(word):
            char_counter = [0] * 26
            for ch in word:
                index = ord(ch) - ord('a')
                char_counter[index] += 1
            return tuple(char_counter)
        
        groups = collections.defaultdict(list)
        
        for word in strs:
            groups[encode(word)].append(word)
        
        return list(groups.values())