class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _remove(self, node):
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

        node.prev = None
        node.next = None

    def _add_to_tail(self, node):
        prev_node = self.tail.prev
        next_node = self.tail
        
        node.prev = prev_node
        node.next = next_node

        prev_node.next = node
        next_node.prev = node


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self._remove(node)
        self._add_to_tail(node)
        return node.value
        

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._remove(node)
            self._add_to_tail(node)
        else:
            node = Node(key, value)
            self._add_to_tail(node)
            self.cache[key] = node

            if len(self.cache) > self.capacity:
                node = self.head.next
                self._remove(node)
                del self.cache[node.key]
            

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)