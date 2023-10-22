class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        out = []
        graph = defaultdict(set)
        in_degree = defaultdict(int)
        
        for course, prereq in prerequisites:
            graph[prereq].add(course)
            in_degree[course] += 1
        
        queue = deque([c for c in range(numCourses) if c not in in_degree])
        
        while queue:
            node = queue.popleft()
            out.append(node)
            
            for nei in graph[node]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    queue.append(nei)
        
        return out if len(out) == numCourses else []
        
        