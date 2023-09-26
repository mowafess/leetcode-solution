class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:

        graph = defaultdict(list)

        for child, parent in zip(pid, ppid):
            graph[parent].append(child)

        res = []
        q = deque([(0, 0 == kill)])
        
        while q:
            node, to_kill = q.popleft()

            if to_kill:
                res.append(node)

            for child in graph[node]:
                q.append((child, to_kill or child == kill))

        return res