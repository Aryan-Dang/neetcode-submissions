class Solution:

    """
    classic BFS problem seems like... as go layer by layer representing the minutes passing...

    return minimum number of mins for all rotten if impossible return -1

    slight twist here would be that instead of iterating first and then starting the BFS we want to start it before and then check for all the number 2s maybe?
    """

    def orangesRotting(self, grid: List[List[int]]) -> int:
        visited = set()
        q = deque()
        next_layer = deque()
        min_count = 0

        #while true loops ensuires that we process the list atleast once to check for all the elements to pass through once and check for 2s...
        while True:
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 2 and (i,j) not in visited:
                        q.append((i,j))
                        visited.add((i,j))

            while len(q) != 0:
                x,y = q.popleft()

                #mark this fruiit as rotten
                grid[x][y] = 2

                #explore all neighbors and add to the next layer to rot

                for n_x, n_y in ((x-1,  y), (x+1, y), (x, y-1), (x, y+1)):
                    #check bounds
                    if n_x > -1 and n_x < len(grid) and n_y > -1 and n_y < len(grid[0]):
                        if grid[n_x][n_y] == 1 and (n_x, n_y) not in visited:
                            visited.add((n_x, n_y))
                            next_layer.append((n_x, n_y))


            if len(next_layer) == 0:
                break
            
            min_count += 1
            
            q = next_layer
            next_layer = deque()

        #quick check to see if all fruits are rotten now...

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        return min_count
        

