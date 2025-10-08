class Node:
    """
    A node in the Trie structure.
    Each node has:
    - children: dictionary mapping characters to child nodes
    - is_terminal_node: boolean flag indicating if this node marks the end of a word
    """
    def __init__(self):
        self.children = {}
        self.is_terminal_node = False


class Trie:
    """
    Trie (Prefix Tree) implementation.
    
    Time Complexity:
    - insert: O(m) where m is the length of the word
    - search: O(m) where m is the length of the word
    - startsWith: O(m) where m is the length of the prefix
    
    Space Complexity: O(n * m) where n is number of words, m is average word length
    """

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        node = self.root

        for ch in word:
            if ch not in node.children:
                node.children[ch] = Node()
            node = node.children[ch]

        node.is_terminal_node = True
        

    def search(self, word: str) -> bool:

        node = self.root

        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]

        return node.is_terminal_node
        

    def startsWith(self, prefix: str) -> bool:

        node = self.root

        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]

        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)