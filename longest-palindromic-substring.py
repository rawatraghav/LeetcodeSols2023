
# o(n^2)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        m = ''  # Memory to remember a palindrome
        for i in range(len(s)):  # i = start, O = n
            for j in range(len(s), i, -1):  # j = end, O = n^2
                if len(m) >= j-i:  # To reduce time
                    break
                elif s[i:j] == s[i:j][::-1]:
                    m = s[i:j]
                    break
        return m


# o(n^2) slightly faster
class Solution:    
    def isPalindrome(self, s: str) -> bool:
        return s == s[::-1]
    
    def longestPalindrome(self, s: str) -> str:
        # so I want to create frames of different lengths
        # that will move along a string
        # so if string is abba
        # the first frame is abba
        # the second iteration be: abb, bba
        # third iteration be: ab, bb, ba
        # we start with widest frame, because we are after longest
        # palindromic substring
        # right off the bat check if the input itself is a non empty palindromic string
        if not s:
            raise Exception("You werent supposed to be null")
            
        if self.isPalindrome(s):
            return s
                
        for i in range(len(s), 0, -1):
            for j in range(0, len(s)-i+1): 
                candidate = s[j:j+i]
                if self.isPalindrome(candidate):
                    return candidate
