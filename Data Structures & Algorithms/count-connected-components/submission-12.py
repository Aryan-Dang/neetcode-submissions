"""
first intuition is that could do the joint intervals thing where we just count the end and beginnings...

i think it's called room scheduler or something

- but doesn't apply here because it's not contiguous... example of [1, 6] and [5,8] would be same interval in the algo above but here it would be different/unconnected...

could do the graph traversal or something too but remembering that pattern so might be worth it...

could construct graph here - that's a cool thing... we have the edges so to be able to do DFS/BFS we have to construct the graph
and then we can keep track

can use the factor that a <= b and that there's no duples to always be that the map key will be the lesser nummber
"""
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {}

        #construct the graph
        for edge in edges:
            x,y = edge
            #relying on the property that x < y so always map x -> y
            #can't rely on this factor actually as in general if we're creating a undirected graph for doing traversal
            #especially when we're relying on checking from 0 -> n then we would need to check if the larger node is in the graph...
            if x not in graph:
                graph[x] = [y]
            else:
                graph[x].append(y)

            if y not in graph:
                graph[y] = [x]
            else:
                graph[y].append(x)
        
        #perform BFS on the graph

        print(graph)

        visited = set()
        q = deque()
        components = 0

        #important catch here need to iterate over n as it could be the case that 
        #n=4 edges=[[2,3],[1,2],[1,3]]

        for key in range(n):
            if key not in visited:
                components += 1
                #everytime we start a new BFS by going to the next non-visited key it's a new component
                q.append(key)
                visited.add(key)

                while len(q) != 0:
                    elem = q.popleft()
                    # print(elem)
                    # if elem not in graph:
                    #     components += 1
                    #     q = deque()
                    #     break
                    # explore neighbors
                    if elem not in graph:
                        q = deque()
                        break
                    for neighbor in graph[elem]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            q.append(neighbor)
        return components


