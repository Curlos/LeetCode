# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        values = []
        self.traverse(root, values)
        return values
    
    def traverse(self, node, values):
        if not node:
            return
        self.traverse(node.left, values)
        values.append(node.val)
        self.traverse(node.right, values)