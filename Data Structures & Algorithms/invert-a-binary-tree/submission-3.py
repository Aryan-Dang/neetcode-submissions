# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
thinking of some sort of a recurisve approach where we call the method on the left and right side 
and then just switch the values

think wht to do with values... why is there anything needed from that one? 
    - so turns out that nothing was needed for that one, we just need to swap left and right values

this solution is in place, no copies realy created... or actually n/2 copies created
"""

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if root is None:
            return None
        
        #invert the left and the right
        rightSubtree = root.right
        leftSubtree = root.left
        root.right = self.invertTree(leftSubtree)
        root.left = self.invertTree(rightSubtree)

        return root