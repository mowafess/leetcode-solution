class Node:
    def __init__(self):
        self.children = {}
        self.is_terminal_node = False

class WordDictionary:

    def __init__(self):
        self.root = Node()
        

    def addWord(self, word: str) -> None:
        node = self.root

        for ch in word:
            if ch not in node.children:
                node.children[ch] = Node()

            node = node.children[ch]
        
        node.is_terminal_node = True
        

    def search(self, word: str) -> bool:
        """
        Search with wildcard support.
        Time: O(26^k) worst case, where k = number of dots
        """
        return self._dfs(word, 0, self.root)
    
    def _dfs(self, word: str, index: int, node: Node) -> bool:

        if index == len(word):
            return node.is_terminal_node
        
        ch = word[index]
        
        if ch == '.':
            # explore all children node if wildcard
            for child in node.children.values():
                if self._dfs(word, index + 1, child):
                    return True
            return False
        else:
            if ch not in node.children:
                return False
            return self._dfs(word, index + 1, node.children[ch])
        