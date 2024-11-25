class Node:
    def __init__(self,key , value):
        self.value = value
        self.next = None
        self.prev = None
        self.key = key


class LRUCache:
    def __init__(self, capacity: int):
        self.d = {}
        self.head = Node(-1,-1)
        self.tail = Node(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
    def deleteNode(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def insertAfterHead(self,node):
        node.next = self.head.next
        self.head.next.prev = node
        node.prev = self.head
        self.head.next = node

    def get(self, key: int) -> int:
        if key in self.d:
            self.deleteNode(self.d[key])
            self.insertAfterHead(self.d[key])
            return self.d[key].value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.d:
            if len(self.d) == self.capacity:
                del self.d[self.tail.prev.key]
                self.deleteNode(self.tail.prev)
        else:
            self.deleteNode(self.d[key])
        new = Node(key,value)
        self.insertAfterHead(new)
        self.d[key] = new
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)