class Solution:
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