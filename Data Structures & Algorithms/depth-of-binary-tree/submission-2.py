# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
intuitive solution seems to be DFS and just maintain max length found at each node... and then just comprae the length
"""

class Solution:

    def calculateSubTreeLength(self, root : Optional[TreeNode], curLen) -> int:
        maxLen = curLen
        if root is not None:
            curLen += 1
            maxLen = max(self.calculateSubTreeLength(root.left, curLen), self.calculateSubTreeLength(root.right, curLen))
        return maxLen

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.calculateSubTreeLength(root, 0)
        