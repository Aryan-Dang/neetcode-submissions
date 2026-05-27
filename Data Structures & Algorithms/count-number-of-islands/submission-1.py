class Solution:
    """
    assumption all indices surrounding the grid is water
    diagnols don't seem to count so only checking horizontal and veritical!! - verified by looking at examples here otherwise would have to clarify!!

    basic solution is looking like bfs yes - important though that we don't explore nodes repeatedly... so maintain visited is important otherwise timing would blow up...

    and have to be sure to iterate through all elements as there could be some disconnected islands for sure...

    how would I know this is graph traversal?  most obvious : the matrix is the graph, thinking of it like a graph because looking at subparts, etc as a graph...
    also traversing the elements implies it's a graph in someways wioth connected and disconnected pieces...

    complexity : O(M*N) as visiting all elements exactly once!
    space : ^

    What was fixed:
The Time Limit Exceeded (TLE) was caused by marking nodes as visited only after they were popped from the queue.

In BFS, if you don't mark a node as visited the moment you append it to the queue, the same coordinate can be added to the queue multiple times from different neighbors before it ever gets processed.
On large grids of '1's, this leads to an exponential explosion of redundant work.
I added visited.add() calls immediately after every q.append() and included a check to ensure we only add a neighbor if it's not already in visited.
Changes:
Moved visited.add() to occur immediately after q.append() and added an if (n_x, n_y) not in visited check to prevent redundant queue entries.
    """
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set() #will store tuples which would be the indices in the grid
        q = deque()
        numIslands = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in visited and grid[i][j] != "0":
                    q.append( (i,j) )
                    while q:
                        currElement = q.popleft()
                        visited.add(currElement) #mark this node as visited
                        x,y = currElement
                        #if grid[x][y] == "1":
                        #important note : only need to start exploring from lands, no need to explore waters....
                        #this also allows easy win condition which is as soon as the len q is empty means we reached end of the land mass and don't need to explore anymore!!!
                        #explore neighbors and add them to the queue
                        for n_x, n_y in ((x-1, y), (x+1, y), (x, y-1), (x, y+1)):
                            #check bounds
                            if n_x > -1 and n_x < len(grid) and n_y > -1 and n_y < len(grid[0]) and grid[n_x][n_y] == "1" and (n_x, n_y) not in visited:
                                #i think below check is redundant as by definition of bfs this would have already been visited and the BFS would never be kicked off from this node agian?
                                # if potential_neighbor not in visited:
                                q.append((n_x, n_y))
                    numIslands += 1

        return numIslands

        