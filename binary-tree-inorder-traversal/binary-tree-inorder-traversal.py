# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        nodes = []
        self.traverse(root, nodes)
        return nodes
    
    def traverse(self, node, nodes):
        if not node:
            return nodes
        
        self.traverse(node.left, nodes)
        nodes.append(node.val)
        self.traverse(node.right, nodes)