# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        values = []
        self.traverse(root, values)
        return values
        
    def traverse(self, root, values):
        if not root:
            return
        
        values.append(root.val)
        self.traverse(root.left, values)
        self.traverse(root.right, values)
            
            
            