class MyLinkedList:

    class Node:
        def __init__(self, e=None):
            self.value = e
            self.next = None

    def __init__(self):
        self.head = self.Node()
        self.tail = self.head
        self.size = 0
        
    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1  # LeetCode convention
        curr = self.head.next
        for _ in range(index):
            curr = curr.next
        return curr.value

    def addAtHead(self, val: int) -> None:
        new_node = self.Node(val)
        new_node.next = self.head.next
        self.head.next = new_node
        if self.size == 0:
            self.tail = new_node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        new_node = self.Node(val)
        self.tail.next = new_node
        self.tail = new_node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return

        if index == 0:
            self.addAtHead(val)
            return 
        if index == self.size:
            self.addAtTail(val)
            return 

        curr = self.head
        for _ in range(index):
            curr = curr.next

        new_node = self.Node(val)
        new_node.next = curr.next
        curr.next = new_node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return

        curr = self.head
        for _ in range(index):
            curr = curr.next

        delete = curr.next
        curr.next = curr.next.next
        delete = None

        if self.size - 1 == index:
            self.tail = curr

        self.size -= 1

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)