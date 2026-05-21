class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        left = 0
        maxy_pooh = 0
        seen = {}
        for right in range(len(s)):
            if s[right] in seen and seen[s[right]] >= left:
                left = seen[s[right]] + 1
            seen[s[right]] = right
            maxy_pooh = max(maxy_pooh, right - left + 1)
        return maxy_pooh

