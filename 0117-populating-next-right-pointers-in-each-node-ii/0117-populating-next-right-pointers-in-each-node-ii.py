"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':

        def leftview(root):
            if not root:
                return []
            
            result = []
            q = deque([root])

            while q:
                n = len(q)
                for i in range(n):
                    node = q.popleft()
                    if i == 0:
                        result.append(node)  # First node of each level

                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            
            return result
        def rightview(root):
            if not root:
                return []
            
            result = []
            q = deque([root])

            while q:
                n = len(q)
                for i in range(n):
                    node = q.popleft()
                    if i == n - 1:
                        result.append(node)  # Last node of each level

                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            
            return result

        def traverse(root):
            if not root : return 
            traverse(root.left)
            traverse(root.right)
            left = leftview(root.right)
            right = rightview(root.left)
            for i in range(min(len(left) , len(right))):
                if right[i]:
                    right[i].next = left[i]
            

            return root


        return traverse(root)
 
        