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
        '''

        results = []
        def DFS(i, target, path) -> None:
            # print(nums[i], target)
            #backtracking condition
            if target < 0 or nums[i] > target:
                return
            if nums[i] == target:
                path.append(nums[i])
                results.append(list(path))
                path.pop()
                return
            for j in range(i, len(nums)):
                path.append(nums[i])
                DFS(j, target - nums[i], path)
                # if tmp:
                #     #found target
                #     if type(tmp[0]) == int:
                #         # print(f"found target with {nums[i]} and tmp : {tmp} and resuls before add : {results}")
                #         results.append([nums[i]] + tmp)
                #         # print(f"results after add : {results}")
                #     else:
                #         for tm in tmp:
                #             results.append([nums[i]] + tm)
                # print(results)
                path.pop()
            return results

        nums.sort()
        # res = []
        #here forgot the edge case of the decision of skipping the very first element itself! should have remembered that we can skip that and should have potentially skipped that as well!
        for i in range(len(nums)):
            DFS(i, target, deque())
            # print(f"main DFS returned : {tmp}")
            # if tmp:
            #     if type(tmp[0]) == int:
            #         res.append(tmp)
            #     else:
            #         res.extend(tmp)
        return results


            

            