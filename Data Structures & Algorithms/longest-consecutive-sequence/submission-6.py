class Solution:
    """
    array of ints -> len longest consecutive sequence
    do not have to be consequtive in the original array
    O(N)
    - not first n numbers otherwise could have used integer sum property
    - O(N) to maintain a set, set lookup is O(1), if appending to a set is a problem initialize a set to a larger num?

    so initial thought is to take the biggest num in the list and iterate backwards from that/check if the number before that is in their and then 

    how to handle duplicates would be a followup/check examples -> dupes don't matter, ignore

    turns out max(nums) doesn't work on empty lists... so special edge case handling think about base case like empty lists etc...

    didn't handle negative nums!! we didn't think about negative nums here...
    iterate from min to max...

    instead of iterating from min to max entirely maybe we can just iterate through the elements of the set...
    """
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        seenNums = set(nums) # O(N)
        maxNum = max(nums)
        minNum = min(nums)
        longestCount = 1
        curCount = 1
        for i in range(minNum, maxNum+1, 1):
            if i+1 in seenNums:
                curCount+=1
            else:
                curCount = 0
            longestCount = max(curCount, longestCount)
        return longestCount


        