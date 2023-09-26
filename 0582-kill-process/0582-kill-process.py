class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:

        graph = defaultdict(list)

        for child, parent in zip(pid, ppid):
            graph[parent].append(child)

        res = []
        q = deque([kill])
        
        while q:
            node = q.popleft()
            res.append(node)

            for child in graph[node]:
                q.append(child)

        return res