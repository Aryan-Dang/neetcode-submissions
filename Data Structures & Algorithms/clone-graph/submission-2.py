class Solution:

    """
    connected undirected graph, deep copy : 

    could probably use DFS to construct a copy...

    important restriction mentioned that there's no dupes and self loops

    each value/graph starts from 1... what is the significance of this?

    recursively build the solution from the original node

    forgot to keep track of visited neighbors/nodes - how to keep track, do we keep track of vals or what? what is the uniqueness factor here? i think they sauid no duplicate edges so that means use neighbors as the tuple for the set....
    """

    """
    What was fixed:
The primary issue was that the visited_nodes set was storing original nodes, but the function was returning those original nodes instead of their copies. This caused the output to contain a mix of original and copied nodes, leading to incorrect structure.

Key fixes:

Changed visited_nodes from a set to a dictionary to map original nodes to their corresponding copyNode. This ensures that if we encounter a node again, we return its existing copy rather than the original or a brand new one.
Removed the redundant copyNode parameter from the function signature.
Mapped the curNode to its copyNode immediately after creation to handle circular references (cycles) correctly.
Removed the explicit check for len(curNode.neighbors) == 0 since the loop naturally handles nodes with no neighbors.
Changes:
Changed visited_nodes to a dictionary to store mappings of {original: copy}, removed the redundant copyNode parameter, and ensured recursiveClone returns the cached copy from the dictionary.
    """
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited_nodes = {}
        return self.recursiveClone(node, visited_nodes)
    
    def recursiveClone(self, curNode, visited_nodes):
        #base case
        if curNode is None:
            return None

        if curNode in visited_nodes:
            return visited_nodes[curNode]
        
        copyNode = Node(curNode.val)
        visited_nodes[curNode] = copyNode

        #explore neighbors
        for neighbor in curNode.neighbors:
            neighborNode = self.recursiveClone(neighbor, visited_nodes)
            if neighborNode is not None:
                copyNode.neighbors.append(neighborNode)
        
        return copyNode