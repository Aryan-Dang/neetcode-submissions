class Solution:
    """
    sorted in non-decreasing order means sorted in increasing order but dupes might exist...

    cannot use the same element twice indices can't be equal so be sure to stop before they're equal!

    how does 1-indexed matter here? what about dupes here?

    """
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i,j = 0, len(numbers) - 1

        while i < j :
            if numbers[i] + numbers[j] == target:
                return [i+1, j+1]
            
            while numbers[i] + numbers[j] > target:
                j -= 1
            while numbers[i] + numbers[j] < target:
                i += 1
        
        return []
            
