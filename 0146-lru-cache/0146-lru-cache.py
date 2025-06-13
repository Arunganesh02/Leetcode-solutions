class Node:
    def __init__(self , value,key ):
        self.val = value
        self.next = None
        self.prev = None
        self.key = key

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.d = {}
        self.head = Node(-1,-1)
        self.tail = Node(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def insertAfterHead(self,node):

        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next  = node

    def deleteBeforeTail(self):
     
        node = self.tail.prev
        self.tail.prev = node.prev 
        node.prev.next = self.tail
        return node.key

    def replaceNode(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def get(self, key: int) -> int:
        if key in self.d:
            node = self.d[key]
            self.replaceNode(node)
            self.insertAfterHead(node)
            return node.val
        else: return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.d:
            node = self.d[key]
            self.replaceNode(node)
            node.val = value
            self.insertAfterHead(node)
            return

        if len(self.d) < self.cap:
            node = Node(value , key)
            self.insertAfterHead(node)
            self.d[key] = node
        else:
            deletedKey = self.deleteBeforeTail()
            node = Node(value,key)
            self.insertAfterHead(node)
            del self.d[deletedKey]
            self.d[key] = node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)