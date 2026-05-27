class Solution:
    """
    all triplets in the nums list where nums[i] + nums[j] + nums[k] == 0, and indices are unique
    no duple triplets so only process each num once?
    could do the same 2 pointer approach but with a narrowing window or something and maintain the hashmap but maybe that's not even needed?

    remembered that have a pointer in the end signifying ending element and then that denotes the end of the window and then we do the 2sum integer 2 approach 
        on a sorted array looking for 0 - nums[k]!
    genius approach remembered by reducing the current problem into one we have solved before already - pattern matching!!

    just do something to prevent dupes -> iterate k back till it's not the same....

    interesting optimization/lifehack for this problem is to iterate the k from the left - my intuition was to fix the number in the end and iterate from the back 
    but they fix the number in the front and iterate in the remaining window - interesting optimization because if nums[k] > 0 then we would never be able to reach zero sum by looking to the right of it...
    makes use of the mention of the fact that we don't want any random sum, we want sum == 0
    good showcase of how it matters to pay attention to the properties and stuff to optimize

    just modified my solution to not trip up here and include this optimization by adding the check...

    one good way of debugging here which I should have remembered is to look at the subwindow for the 3sum being considered because k is fixed to be the third/last element so helps narrow down and walk through the example being considered!!
    """
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        k = len(nums) - 1
        nums.sort()
        while k > -1 and nums[k] > -1:
            i,j = 0, k-1
            target = 0-nums[k] #now the problem has been decomped into the problem we had before
            while i < j and j < k:
                if nums[i] + nums[j] == target:
                    res.append([nums[i], nums[j], nums[k]])
                    i += 1

                    #increment i while avoiding dupes
                    while i < j and nums[i] == nums[i-1]:
                        i += 1

                    j -= 1
                    while j > -1 and nums[j] == nums[j+1]:
                        j -= 1
                    
                while nums[i] + nums[j] > target and i < j:
                    j -= 1
                while nums[i] + nums[j] < target and i < j:
                    i += 1
            j = k - 1
            while nums[j] == nums[k] and j > 0:
                #realized that the cool way here would be to just move j back till it's not equal to k and then set k to that!
                j -= 1
            k = j
            
        return res
