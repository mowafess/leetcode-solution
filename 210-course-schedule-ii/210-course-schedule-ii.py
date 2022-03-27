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
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """

        # Prepare the graph
        adj_list = defaultdict(list)
        indegree = {}
        for dest, src in prerequisites:
            adj_list[src].append(dest)

            # Record each node's in-degree
            indegree[dest] = indegree.get(dest, 0) + 1

        # Queue for maintainig list of nodes that have 0 in-degree
        zero_indegree_queue = deque([k for k in range(numCourses) if k not in indegree])

        topological_sorted_order = []

        # Until there are nodes in the Q
        while zero_indegree_queue:

            # Pop one node with 0 in-degree
            vertex = zero_indegree_queue.popleft()
            topological_sorted_order.append(vertex)

            # Reduce in-degree for all the neighbors
            if vertex in adj_list:
                for neighbor in adj_list[vertex]:
                    indegree[neighbor] -= 1

                    # Add neighbor to Q if in-degree becomes 0
                    if indegree[neighbor] == 0:
                        zero_indegree_queue.append(neighbor)

        return topological_sorted_order if len(topological_sorted_order) == numCourses else []