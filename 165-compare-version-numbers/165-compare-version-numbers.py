class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v2 = version2.split('.')
        
        i = j = 0
        
        while i < len(v1) or j < len(v2):
            if i >= len(v1):
                curr1 = 0
            else:
                curr1 = int(v1[i])
                
            if j >= len(v2):
                curr2 = 0
            else:
                curr2 = int(v2[j])
                
            if curr1 < curr2:
                return -1
            elif curr1 > curr2:
                return 1
            
            i += 1
            j += 1
            
        
        return 0
            
            
            
            
        