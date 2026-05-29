class Solution:
    """
    important that border things aren't considered as surrounded regions

    four directionaly connected meaning don't consider diagnols!!

    four directionally means that we can have the start and end index of the rectangle which is the group 0s
    and then once found just convert all these to x...

    had to confirm that this just means connected up/down or left/right

    narrowed it down by recognizing that most graph probelms come down to traversal whcih is dfs and bfs!!

    almost forgot the edge case of the border ones... remember that...

    maybe could use the trick here that we extend the board 

    AAHAHHHHHH TOTALLY MISSED THE HINT THAT BASICALLY AS LONG AS THERE IS NO PATH FROM THE EDGE TO ANY OF THE COMPONETS IN THE CENTER THEN IT'S OK HOLYYY

    so just need to launch DFS from every 0 on the edge and the check if DFS leads to any of the nodes in the center... if it does then we mark those nodes in safe set and then skip marking those as "X"

    doesn't even need to be DFS just has to be graph traversal...

    also don't need to maintain a visited list actually... realized the optimization for graph/grid related problems is that can just modify state in-place instead of maintaining separate list...

    small bug here... used to check for "0" "O" 

    also forgot the important pattern that we should be marking them as temporary and not gone completely...
    because that means that they are safe
    so we should be marking them as T and the Ts stay as Os and the Os become x...
    """
    def solve(self, board: List[List[str]]) -> None:

        def DFS(i,j):
            #mark the node we're exploring right now as 'visited' so mark it as "X"
            board[i][j] = "T"

            #explore the neighbors
            for (x,y) in ( (i-1, j), (i+1, j), (i, j-1), (i, j+1)):
                if x > -1 and x < len(board) and y > -1 and y < len(board[0]):
                    #check if coordinates are 'visited' by checking if they '0'
                    if board[x][y] == "O":
                        #need to ensure that we mark as visited before adding to the stack/queue/launching recursion as otherwise could end up exploring cycles...
                        board[x][y] = "T"
                        DFS(x,y)

        #checking the top and bottom rows
        for j in range(len(board[0])):
            if board[0][j] == "O":
                DFS(0,j)
            if board[len(board)-1][j] == "O":
                DFS(len(board)-1, j)
        
        for i in range(len(board)):
            if board[i][0] == "O":
                DFS(i, 0)
            if board[i][len(board[0])-1] == "O":
                DFS(i,len(board[0])-1)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "T":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"

