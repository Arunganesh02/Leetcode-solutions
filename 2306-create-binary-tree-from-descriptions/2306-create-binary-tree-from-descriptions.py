# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        d = {}
        parent = {}
        for i in descriptions:

            if i[0] not in d:
                newnode = TreeNode(i[0])
                d[i[0]] = newnode
                parent[i[0]] = 1
            else:
                newnode = d[i[0]]

            if i[1] not in d:
                child = TreeNode(i[1])
                d[i[1]] = child
                parent[i[1]] = 2
            else:
                child = d[i[1]]
                parent[i[1]]  += 1
            # print(d)
            if i[2] == 1:
                newnode.left = child
            else:
                newnode.right = child
        # print(parent)
        for i in parent:
            if parent[i] == 1:
                return d[i]