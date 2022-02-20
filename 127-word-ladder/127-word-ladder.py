from string import ascii_letters

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        def generate_graph(word_list):
            graph = defaultdict(set)
            
            for word in word_list:
                for i in range(len(word)):
                        graph[word[:i] + "*" + word[i+1:]].add(word)

            return graph
        
        def word_ladder(begin: str, end: str, word_list: List[str]) -> int:
            if not word_list or not begin or not end or end not in word_list:
                return 0
            
            graph = set(word_list)

            q = deque([(begin, 1)])
            visited = set(begin)

            while q:
                node, level = q.popleft()
                
                for i in range(len(node)):
                    for c in ascii_letters:
                        nei = node[:i] + c + node[i+1:]
                        if nei in graph:
                            if nei == end:
                                return level + 1
                            if nei not in visited:
                                q.append((nei, level + 1))
                                visited.add(nei)

            return 0
        
        return word_ladder(beginWord, endWord, wordList)
