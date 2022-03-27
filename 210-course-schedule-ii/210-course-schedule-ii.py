class Solution:
    # def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
#         graph = defaultdict(set)
#         visited = {}
#         output = []

#         for course, prereq in prerequisites:
#             graph[prereq].add(course)

#         def dfs(c):
#             if c in visited:
#                 return visited[c]

#             visited[c] = True

#             for others in graph[c]:
#                 if dfs(others):
#                     return True

#             visited[c] = False
#             output.append(c)


#         for course in range(numCourses):
#             if dfs(course):
#                 return []

#         return output[::-1]
        
        
    def findOrder(self, numCourses, prerequisites):

        graph = defaultdict(list)
        indegree = {}
        for dest, src in prerequisites:
            graph[src].append(dest)
            indegree[dest] = indegree.get(dest, 0) + 1

        zero_indegree_queue = deque([k for k in range(numCourses) if k not in indegree])

        topological_sorted_order = []

        while zero_indegree_queue:
            
            node = zero_indegree_queue.popleft()
            topological_sorted_order.append(node)

            if node in graph:
                for neighbor in graph[node]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        zero_indegree_queue.append(neighbor)

        return topological_sorted_order if len(topological_sorted_order) == numCourses else []