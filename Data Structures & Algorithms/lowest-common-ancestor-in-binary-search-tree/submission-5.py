# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
it's a binary search tree which means/implies/indicates the relation...

Left Subtree: All nodes in the left subtree of \(X\) must have key values less than the value of \(X\).Right Subtree: All nodes in the right subtree of \(X\) must have key values greater than the value of \(X\).

also mentioned that all nodes are unique...

so lowest common ancestor which has this node as the parent

thinking about backtracking solution here 

was clueless here but knew that has to be some sort of a depth first/bread first solution here so gonna focus on that = then think about optimization later...

thinking of a solution here where do depth first search and then once we found both the nodes we see what to do...

example 1:

found 4 continue - don't see 2

actually realized that doing layer by layer BFS could work here potentially...?

the hints were helpful... using the property of left and right path we can decide which path to use...


so recurisve solutino would follow the logic they mentioend - if split occurs then current node is the lca seen so far
if both are in thd same subtree then LCA lies in that subtree and we have to traverse that tree to find it...

a little confused how we decipher which node is lower ancestor? - i don't think we would ever need to do this...
"""

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        if root is None:
            return None

        def search(node, p, q, currentLCA : TreeNode):
            if node is None:
                return currentLCA

            if node.val == q.val or node.val == p.val:
                currentLCA = node 

            #traverse the right subtree to check for it...
            elif node.left is None or (p.val > node.val and q.val > node.val):
                currentLCA = search(node.right, p, q, currentLCA)
                
            elif node.right is None or (p.val <= node.val and q.val <= node.val):
                currentLCA = search(node.left, p, q, currentLCA)
            
            #case that we have both the trees available...
            #splitting at this node, this node could be the LCA
            elif (p.val <= node.val <= q.val) or (q.val <= node.val <= p.val):
                currentLCA = node

            return currentLCA

        return search(root, p, q, root)

                    




