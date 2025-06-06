# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.se = set()
        def traverse(root, run):
            left = (run*2) +1
            right = (run * 2) + 2
            self.se.add(run)
            if root.left : traverse(root.left , left)
            if root.right : traverse(root.right , right)
        traverse(root , 0)
    def find(self, target: int) -> bool:
        if target in self.se:
            return True
        else: return False
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)