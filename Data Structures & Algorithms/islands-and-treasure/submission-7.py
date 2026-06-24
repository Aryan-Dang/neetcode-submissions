class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        '''
        similar approach to the rotten oranges problem where we just do the layer by layer and can replace the thing in-memory
        '''
        layer = deque()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    layer.append((row, col))
        min_dist_from_treasure = 0
        next_layer = deque()
        while True:
            # print(layer)
            min_dist_from_treasure += 1
            #explore neighbors of all the elements in this layer and add neighbors to next layer and mark these as the distance
            while len(layer) != 0:
                i,j = layer.pop()
                # print(len(layer) != 0, i, j)
                #explore valid neighbors
                for (x,y) in ((i-1, j), (i+1, j), (i, j-1), (i, j + 1)):
                    if x > -1 and x < len(grid) and y > -1 and y < len(grid[0]):
                        # print(x,y, grid[x][y])
                        # if math.isinf(grid[x][y]):
                        if grid[x][y] == 2147483647:
                            # print(grid[x][y] == 2147483647)
                            #mark this node as explored (mark the distance) and then put it into next_layer for exploration perhaps?
                            grid[x][y] = min_dist_from_treasure
                            next_layer.append((x,y))
            layer = next_layer
            next_layer = deque()
            if len(layer) == 0:
                break
        

