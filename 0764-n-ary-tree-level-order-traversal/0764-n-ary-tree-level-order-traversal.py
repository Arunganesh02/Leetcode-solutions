"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        que = [root]
        if root is None : return []
        ans = [[root.val]]
        while len(que)!= 0:
            l = len(que)
            temp = []
            for i in range(l):
                p = que[0]
                que.pop(0)
                for i in p.children:
                    if i is not None:
                        que.append(i)
                        temp.append(i.val)
            if len(temp) != 0:
                ans.append(temp)
        return ans