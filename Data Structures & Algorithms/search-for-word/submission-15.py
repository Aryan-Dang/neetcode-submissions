class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        '''
        approach I'm thinking of here is to start DFS from each index... launch backtracking if at the ith step, we're equal to the ith letter and then recurse to neighbors... if we 

        important realization is that since we're in single threaded environment, even though we have the recursive search space/tree everything happens sequentially sow e can use a variable oputside of the DFS call
        for maintaining the state/path - we don't need to pass it in every call!

        realized that we don't even need to maintian the path, can simply rely on only forwarding the exploration if the row col match!
        also realized that we need to maintain visited set for each search separately, can't share state there!

        ran into a small bug where we found the word(meaning algorithm correct) but exists not getting updated some reason? seems like weird bug where usually if it was a object it coulda been accessed inside the function but not if it's a boolean? check this via claude and verify if this true or not for Python?

        also missing the edge case for 
        '''

        #IMP - do not forget the visited set to prevent visiting the same letter!!

        exists = False

        def DFS(row, col, index, visited) -> None:
            nonlocal exists
            if index == len(word):
                # print('found word!!')
                exists = True
                return
            if board[row][col] == word[index]:
                # print(board[row][col], index, [board[i][j] for (i,j) in visited])
                #current index match, proceed with the search from remaining
                visited.add((row, col))
                index += 1
                #need a check in case we're at the last element/can't check any other elements yet we just found it so we can't launch a new search...
                if index == len(word):
                    exists = True
                    return
                #explore neighbors
                for (i, j) in ((row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)):
                    if i > -1 and i < len(board) and j > -1 and j < len(board[0]):
                        # print(f"considering neighbor : {board[i][j]}")
                        if (i,j) not in visited:
                            # print(f"launching call to neighbor : {board[i][j]}")
                            DFS(i, j, index, visited)
                            # print(f'value of exists after that call : {exists}')
                visited.remove((row,col))
            return
        for row in range(len(board)):
            for col in range(len(board[0])):
                DFS(row, col, 0, set())
                if exists:
                    return exists

        return exists