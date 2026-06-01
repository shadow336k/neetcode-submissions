class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        longest = 0
        seen = {} # char:index
        left = 0
        right = 0
        for right in range(len(s)):
            current_char = s[right]
            if current_char in seen and seen[current_char] >= left:
                left = seen[current_char] + 1
            seen[current_char] = right
            longest = max(longest, right - left + 1)
        return longest
# abcabcbb 
# abcabcba
#a:0
#b:1
#c:2