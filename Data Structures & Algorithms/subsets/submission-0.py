class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for i in range(len(nums)):
            temp_hold = []
            for res in result:
                temp_hold.append(res + [nums[i]])
            result += temp_hold
        return result