class Solution:
    """
    Remembered solution somewhat that have to maintain a prefix product list and postfix product list... and then just multiply indicis

    edge case emptyy list
    edge case first and last indice

    came up wiht the relation that prefixProduct[i] = prefixProduct[i-1] * nums[i-1] (as prefix[i] represents the product of everything before ith index!!)
    counter true for postProduct[i] -> it reperesnts everything after the ith index
    non-inclusive is important!!!

    iterating from 1, len(nums) skips 0th index which means last and first index are skipped and default value of 1 is used... for empty case, we should exit early and return empty

    for [0] -> 1 might make sense as the product of no elements would be 1? idk how is this defined?
    """
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        if len(nums) == 0:
            return []

        preProd = [1 for num in nums]
        postProd = [1 for num in nums]

        for i in range(1, len(nums)):
            preProd[i] = preProd[i-1] * nums[i-1]
            postProd[len(nums)-1-i] =  postProd[len(nums)-i] * nums[len(nums)-i]
        
        return [preProd[i]*postProd[i] for i in range(len(nums))]