class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word: str):
        node = self.root

        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()

            node = node.children[ch]

        node.end = True

    def shortest_prefix(self, word: str) -> bool:
        node = self.root

        for i, ch in enumerate(word):
            # no matching prefix
            if ch not in node.children:
                return word
            
            # move to next node
            node = node.children[ch]

            if node.end:
                return word[:i+1]

        return word


class Solution:
    """
    Time complexity: O(d⋅w+s⋅w)
    Creating the Trie takes O(d⋅w). Creating the data structure that stores the words in the sentence takes O(s⋅w).
    
    Space - O(N × M × A)
    N = number of words
    M = average word length
    A = alphabet size (26 for lowercase English)

    """
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        words = sentence.split()
        trie = Trie()
        for word in dictionary:
            trie.add(word)

        return ' '.join(trie.shortest_prefix(word) for word in words)
        