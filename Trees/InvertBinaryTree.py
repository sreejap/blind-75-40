# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# The core concept involves utilizing post-order traversal to swap child pointers at each node level recursively.
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        
        root.left = self.invertTree (root.left)
        root.right = self.invertTree (root.right)

        root.left, root.right = root.right, root.left

        return root
      
