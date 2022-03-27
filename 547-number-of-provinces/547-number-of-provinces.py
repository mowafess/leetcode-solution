class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        """ T - N^2, s - N (max size of the visited)"""
        def dfs(start):
            visited.add(start)
            for end in range(len(isConnected)):
                if end not in visited and isConnected[start][end]:
                    dfs(end)
        
        numberOfProvinces = 0
        visited = set()
        
        for start in range(len(isConnected)):
            if start not in visited:
                numberOfProvinces += 1
                dfs(start)
        
        return numberOfProvinces
    
            
        
        