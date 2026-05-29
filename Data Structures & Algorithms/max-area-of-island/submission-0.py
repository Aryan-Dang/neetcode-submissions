class Solution:
    """
    so. we're given the grid so we know that we don't need to create the graph/adjacency list
    no diagnol connections count

    so solution I'm thinking of is BFS and then keep track of each area from each bfs and then just do check the max
    """
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        stack = deque()
        maxArea = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in visited and grid[i][j] == 1:
                    #starting BFS so will compare the area here!
                    visited.add( (i,j) )
                    stack.append( (i,j) )

                    curArea = 0
                    #attempting DFS right now
                    while len(stack) != 0:
                        x,y = stack.pop()
                        curArea += 1
                        #explore neighbors

                        for (n_x, n_y) in ((x-1, y), (x+1, y), (x, y-1), (x, y+1)):
                            if n_x > -1 and n_x < len(grid) and n_y > -1 and n_y < len(grid[0]):
                                #check visited nodes
                                if (n_x, n_y) not in visited and grid[n_x][n_y] == 1:
                                    visited.add((n_x, n_y))
                                    stack.append((n_x, n_y))
                    maxArea = max(maxArea, curArea)
        
        return maxArea


