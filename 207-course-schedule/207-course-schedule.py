class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # find cicular ref
        
        graph = collections.defaultdict(set)
        
        for course, prerequisite in prerequisites:
            graph[course].add(prerequisite)
           
        def dfs(course):
            if visited[course]:
                return False
            if not graph[course]:
                return True
            
            visited[course] = 1
            result = True
            
            for prereq in graph[course]:
                if not dfs(prereq):
                    return False
                
            visited[course] = 0
            graph[course] = set()
            
            return True
            
        visited = [0] * numCourses
        
        for course in range(numCourses):
            if not dfs(course): return False
        return True