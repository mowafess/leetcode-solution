class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        groups = collections.defaultdict(list)
        
        for word in strs:
            groups[tuple(sorted(word))].append(word)
        
        return list(groups.values())