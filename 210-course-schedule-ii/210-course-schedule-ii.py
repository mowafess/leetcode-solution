class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = defaultdict(set)
        visited = {}
        output = []

        for course, prereq in prerequisites:
            graph[prereq].add(course)

        def dfs(c):
            if c in visited:
                return visited[c]

            visited[c] = True

            for others in graph[c]:
                if dfs(others):
                    return True

            visited[c] = False
            output.append(c)


        for course in range(numCourses):
            if dfs(course):
                return []

        return output[::-1]
        