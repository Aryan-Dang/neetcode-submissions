class Solution:
    '''
    same thing as the original problem just basically have to check the ending one as well...
    can just add an extra value at the end of the last one for the first one
    also have to add one to the beginning tho right?

    money(j) : max(money(j-1), nums[j] + money(j-2))

    actually this doesn't work fully as in the 3,4,3 example can't rob either 3s as it surrounds it!

    maybe we should be building from the middle? actually just doing edge case monkey business...

    3. Dynamic Programming (Bottom-Up)

Intuition
This is House Robber II (circular houses) solved using Bottom-Up Dynamic Programming.

Because houses are in a circle, you cannot rob both the first and last house.
So we split the problem into two linear cases:

Rob houses from index 1 to n-1 (exclude first house)
Rob houses from index 0 to n-2 (exclude last house)
Each case becomes the normal House Robber I problem.

Common Pitfalls

Forgetting the Single House Edge Case
When there is only one house, the circular constraint does not apply since there is no adjacency conflict. If you split the problem into nums[1:] and nums[:-1] without handling this case, both subarrays become empty when n=1, and the function returns 0 instead of nums[0]. Always check if the array has only one element and return its value directly.

Incorrectly Handling the Circular Constraint
The key insight is that the first and last houses cannot both be robbed. A common mistake is to add complex flag logic throughout the recursion when a simpler approach exists: run the standard House Robber algorithm twice, once excluding the first house and once excluding the last house. Taking the maximum of these two results correctly handles the circular dependency without overcomplicating the code.

Off-by-One Errors in Array Slicing
When splitting the array into nums[1:] (exclude first) and nums[:-1] (exclude last), be careful with language-specific slicing syntax. In some languages, you need to manually copy subarrays or adjust loop bounds. An off-by-one error here can lead to including both the first and last houses in one subproblem, or excluding more houses than intended, producing incorrect results.
    '''
    # def rob(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     #sad reality is that had to play around and debug to figure out the exact values to use in the loop - ideally would have figured this out by walking through the code/list but did a little bit of bruteforcing as in a rush
    #     nums_updated = [nums[i-1] if i != -1 and i <= n else 0 for i in range(n+2)]
    #     nums_updated[0] = nums[-1]
    #     nums_updated[n+1] = nums[0]
    #     #nums_updatded should be straight list now but padded
    #     print(nums_updated)
    #     m = len(nums_updated)
    #     money = [0 for i in range(m+2)]
    #     for i in range(2, m):
    #         money[i] = max(money[i-1], nums_updated[i-2] + money[i-2])
    #     #important learning after coding round at Ramp - debug outside of if statmeents, try and except blocks etc... mainly try doing outside
    #     print(money)
    #     return money[n]

    def rob(self, nums: List[int]) -> int:

        '''
        Helper code to do House robber 1 on subset of the array...
        same recurrence as before, money(j) : max(money(j-1), nums[j] + money[j-2])
        '''
        def performSearch(nums : List[int]):
            n = len(nums)
            money = [0 for i in range(n+2)]
            for j in range(2,n+2):
                money[j] = max(money[j-1], nums[j-2] + money[j-2])
            return money[n+1]

        if len(nums) == 1:
            return nums[0]

        return max(performSearch(nums[1:]), performSearch(nums[:-1]))


        