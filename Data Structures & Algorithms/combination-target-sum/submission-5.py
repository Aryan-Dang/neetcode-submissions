class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        '''
        key here is that the same number can be chosen any amount of times which simply implies that we would only backtrack if we exceeded the sum

        2 <= nums[i] <= 30 no negative all > 1

        backtracking/tree problem as generating the search space and heading back/eliminating based on conditions

        don't need to create set manually as all nums in there are unique

        key here is that if we sort it once we know that adding a number made it bigger than the target we can stop!!

        sketch out the decision tree made me realize that we don't need to keep track of the results within the dfs if we keep reduicing the target we are looking for...
        and other important trick i rmeembered is that if recursion is starting from index i, it should never need to access anything before it because those numbers would be considered int he searches before as the order of the combination doesn't matter so those elements would for sure be captured in the search before

        so if we search and then stop searching as soon as the current number is bigger than the target we can prune this by a ton!
        so my recursive approach was correct, just messy implementation, need to clean up the way i'm merging the results/managing the state
        messy because I realized that would be returning a compunding/maintained list so need to update the format there...

        instead can maintain result/path in the DFS and then just append to results once we found the target - supplment this with reasoning above from claude

        the deque implementation with results maintained made it very very clean as we could visualize the path very very easily in our head with the deque object and the results object being maintained cleanly to the side
        this inspires cleaner coding practice by using appropriate data structures to visualize things
        '''

        results = []
        def DFS(i, target, path) -> None:
            if target < 0 or nums[i] > target:
                return
            if nums[i] == target:
                #be sure to add the current num to the path to ensure we include it in the result
                path.append(nums[i])
                #create the copy and add to result - copy needed so that we don't mess up when we manipulate the path we're taking
                results.append(list(path))
                #pop because we explored this path and wouldn't want to keep this number in the path and make the path ready for the next exploration
                path.pop()
                return
            path.append(nums[i])
            for j in range(i, len(nums)):
                DFS(j, target - nums[i], path)
            path.pop()
            return results

        nums.sort()
        #here forgot the edge case of the decision of skipping the very first element itself! should have remembered that we can skip that and should have potentially skipped that as well!
        for i in range(len(nums)):
            if nums[i] > target:
                break
            DFS(i, target, deque())
        return results


            

            