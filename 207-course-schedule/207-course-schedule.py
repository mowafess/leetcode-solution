class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        total = 0
        graph = defaultdict(set)
        in_degree = defaultdict(int)
        
        for course, prereq in prerequisites:
            graph[prereq].add(course)
            in_degree[course] += 1
        
        queue = deque([c for c in range(numCourses) if c not in in_degree])
        
        while queue:
            node = queue.popleft()
            total += 1
            
            for nei in graph[node]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    queue.append(nei)
        
        return numCourses == total
        
        # find cicular ref
        
#         graph = collections.defaultdict(set)
        
#         for course, prerequisite in prerequisites:
#             graph[course].add(prerequisite)
           
#         def dfs(course):
#             if visited[course]:
#                 return False
#             if not graph[course]:
#                 return True
            
#             visited[course] = 1
#             result = True
            
#             for prereq in graph[course]:
#                 if not dfs(prereq):
#                     return False
                
#             visited[course] = 0
#             graph[course] = set()
            
#             return True
            
#         visited = [0] * numCourses
        
#         for course in range(numCourses):
#             if not dfs(course): return False
#         return True