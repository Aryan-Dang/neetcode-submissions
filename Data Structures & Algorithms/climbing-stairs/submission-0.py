class Solution:
    def climbStairs(self, n: int) -> int:
        ways = [1 for i in range(n+2)]
        for i in range(2, n+2):
            ways[i] = ways[i-1] + ways[i-2]

        return ways[n]
