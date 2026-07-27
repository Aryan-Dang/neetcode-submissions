class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        longestCount = 0
        curCount = 0

        left,right = 0,0

        while right < len(s):
            if s[right] not in seen:
                curCount += 1
                seen.add(s[right])
            else:
                #process first
                longestCount = max(longestCount, curCount)
                while s[right] in seen:
                    seen.remove(s[left])
                    left += 1
                    curCount -= 1
                seen.add(s[right])
                curCount += 1
            right += 1
        
        return max(longestCount, curCount)