class Solution:
    '''
    seems like a copy of the prev. problem basically
    use the description to come up with recurrence
    '''
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        ways = [0 for i in range(n+2)]
        for i in range(2,n+2):
            ways[i] = cost[i-2] + min(ways[i-1], ways[i-2])
        print(ways)
        return min(ways[n], ways[n+1])