
# https://leetcode.com/problems/prime-palindrome/description/

# Brute Force
class Solution:
    def primePalindrome(self, k: int) -> int:
        
        # smallest prime palindrome

        def is_prime(n):

            if n < 2:
                return False

            for i in range(2, int(n**0.5)+1):
                if n%i == 0:
                    return False
            return True
        
        def is_palindrome(n):
            return str(n) == str(n)[::-1]

        while True:
            if 10**7 < k < 10**8:
                k = 10**8
            if is_prime(k) and is_palindrome(k):
                return k
            k = k + 1

# 