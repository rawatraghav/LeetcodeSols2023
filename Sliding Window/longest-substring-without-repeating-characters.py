

# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/


# Best Solution

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if s == "":
            return 0

        l = 0
        r = 1
        ans = 1
        sub = 1

        while r < len(s):

            if s[r] not in s[l:r]:
                ans += 1
                r += 1
            else:
                while s[r] in s[l:r] and l < r:
                    l += 1
                    ans -= 1
            sub = max(ans, sub)
        
        return sub