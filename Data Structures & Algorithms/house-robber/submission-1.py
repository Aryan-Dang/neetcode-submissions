class Solution:
    '''
    importnat pointer : houses are in a straight line so there's no cirlces so you don't have to check around the corner/loop around...
    so basically can't rob adjacent houses... so recurrence comes out to be
    money(j) : max(nums[j] + nums[j-2], nums[j-1])
    again same pattern which is that building up recursively based on what we would do for the jth index and the rest just builds up and is setup automatically
    '''
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        money = [0 for i in range(n+2)]
        for i in range(2, n+2):
            money[i] = max(nums[i-2] + money[i-2], money[i-1])
        return money[n+1]
        