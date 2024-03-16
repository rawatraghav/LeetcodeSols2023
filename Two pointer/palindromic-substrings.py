
# https://leetcode.com/problems/palindromic-substrings/description/

class Solution:
    def countSubstrings(self, s: str) -> int:
        # Helper function to expand from the center
        def expandFromCenter(s, left, right):
            count = 0
            # Check for palindrome while staying within string boundaries
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            return count

        count = 0
        for i in range(len(s)):
            # Check for odd length palindromes
            count += expandFromCenter(s, i, i)
            # Check for even length palindromes
            count += expandFromCenter(s, i, i + 1)

        return count