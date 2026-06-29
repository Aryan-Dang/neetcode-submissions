class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        '''
        again, writing this down was really really helpful as I was able to decompose the problem and notice that we have to just generate all valid pairs and can even cache/memoize stuff as repeated calculations would happen

        broke this down into DP as saw recurrence/instances of being stuff being recomputer!!
        didn't get backtracking persay here as couldn't map the pronlem into search space which is crucial for for backtracking! would probably think of some way to think of state and remaing state if we take j amount of "(" and ")" andd then the remaining ones...

        so seems like missing a crucial part of the recurrence : need to include that to build the actual solution out and also important to recognize the fact that if this happens should be able to recouperate and reattempt/continue the solution

        as for the backtracking solution, it's pretty straightforward and the condiiton i was thinking of is simple, keep track of open count and close count and only valids are when close <= open <= n and the stopping count == when we have reached the end is when open == close == n, that's a valid option and we have reached the end so we can add it to results - same solution would apply here, we would want to create the path as before and maintain backtracking steps etc as intended before...
        for backtracking to make the actual decision tree had to decide what the decision i was making at each step was : this is the crucial part of backtracking problems and it is what the decision tou have to make at each step
        by drawing the tree on paper, realize that the option we have at each step is whether to close the previous or keep the current open and add a farther open in there...
        '''

        ##### old approach

        # OPT = [[] for _ in range(n+1)]
        
        # for i in range(1, n+1):
        #     if i == 1:
        #         #base case : ()
        #         OPT[i] = ["()"]
        #     #should have been thinking about why repeats are happening but instead thinking of using set... important to understand problem in my recurrence instead jumping to the bandaid solution of removing dupes perhaps...
        #     #not sure if it would be possible to do this without maintaining set... -> it is with the right recurrence which based on my understanding later I figured out...
        #     else:
        #         res = set()
        #         for valid_parenthesis in OPT[i-1]:
        #             res.add(f"({valid_parenthesis})")
        #             res.add(f"{valid_parenthesis}()")
        #             res.add(f"(){valid_parenthesis}")
        #         OPT[i] = list(res)
        #         print(f"OPT after appending at {i} : {OPT}")
        # return OPT[n]

        #### updated recurrence DP approach

        OPT = [[] for _ in range(n+1)]
        print(OPT)

        OPT[0].append("")
        for k in range(1, n+1):
            res = []
            for i in range(k):
                print(i, k)
                for left in OPT[i]:
                    for right in OPT[k-1-i]:
                        generated = f"({left}){right}"
                        print(left, right, i, k, generated)
                        if generated:
                            res.append(generated)
            OPT[k].extend(res)
        print(OPT)
        return OPT[n]
                

        ##### backtracking attempt!

        # result = []
        # #same generic DFS backtracking algo as before
        # def DFS(opened, closed, path) -> None:
        #     if closed > opened or opened > n:
        #         return
        #     if opened == closed and opened == n:
        #         #case of adding the result, depends on how we are keeping track of the ()
        #         print(opened, path)
        #         if path and path[-1] == "(":
        #             #add the extra closing ')' and then add to results
        #             path.append(')')
        #             result.append(list(path))
        #             #remove this so that we can continue iterating without closing
        #             path.pop()
        #             return
        #         else:
        #             result.append(list(path))
        #             return
        #     #now making the decision of opening a new one vs closing the previous one
        #     #open new one
        #     path.append("(")
        #     DFS(opened-1, closed-1, path)
        #     #closing this one and calling then
        #     path.append(")")
        #     DFS(opened-1, closed-1, path)

        # DFS(0, 0, deque())
        # return result