class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_len = 0
        seen = set()
        for right in range(len(s)):
            char=s[right]
            while char in seen:
                seen.remove(s[left])
                left+=1
            seen.add(char)
            max_len = max(max_len, right - left + 1)
        return max_len