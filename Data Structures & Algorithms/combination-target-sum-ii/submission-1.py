class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
        may contain duplicates!!
        all unique combinations, each number may be chosen only once! no dupes!

        writing it down made me realize that we should skip the dupes within the inner loop - more details from the code!
        '''

        results = []
        #same boiler plate for DFS backtracking!
        def DFS(i, target, path):
            if i >= len(candidates) or candidates[i] > target:
                return
            if candidates[i] == target:
                #found target do the path stuff
                path.append(candidates[i])
                results.append(list(path))
                path.pop()
                return
            
            #actual exploration - important caveat that we skip the current number as we can't reuse
            #using while loop allows us to easily skip dupe numbers from within the loop as we can only use the number once...
            j = i+1
            #same logic as combination sum 1, add candidates[i] because we are subtracting candidates[i] from target
            path.append(candidates[i])
            while j < len(candidates):
                #looking for new target from the current index with the current path
                DFS(j, target - candidates[i], path)
                #now the unique part which is to skip dupes adjacent and keep cycling till we can find the next unique num!
                next_j = j + 1
                while next_j < len(candidates) and candidates[j] == candidates[next_j]:
                    next_j += 1
                j = next_j

            #reiterating mental note but using the deque here helped translate the logi I was thinking of walking down a path into code as using the path stack to maintain the path!!
            path.pop()
            return
        
        candidates.sort()
        #have to do the same logic of skipping the dupe candidates here as well!
        i = 0
        while i < len(candidates):
            DFS(i, target, deque())
            next_i = i + 1
            while next_i < len(candidates) and candidates[i] == candidates[next_i]:
                next_i += 1
            i = next_i
        return results