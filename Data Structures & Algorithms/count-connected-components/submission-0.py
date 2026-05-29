from collections import defaultdict

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # thinking to build a graph first
        # then do an exploration, keeping track of visited.
        # do dfs on all of them, and when I encounter a node that has not been visited, inc

        graph = defaultdict(set)

        for edge in edges:
            graph[edge[0]].add(edge[1])
            graph[edge[1]].add(edge[0])

        visited = set()
        count = 0

        def explore(node):
            if node in visited:
                return
            else:
                visited.add(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    explore(neighbor)

        for temp_node in range(n):
            if temp_node not in visited:
                count += 1
                explore(temp_node)

        return count