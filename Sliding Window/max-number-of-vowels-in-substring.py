
# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/description/?envType=study-plan-v2&envId=leetcode-75


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        vows = 'aeiou'
        length = len(s)
        counter = 0

        for ch in s[:k]:
            if ch in vows:
                counter += 1

        max_count = counter
        
        for i in range(k, length):
            if s[i-k] in vows:
                counter -= 1
            if s[i] in vows:
                counter += 1
            max_count = max(counter, max_count)
        
        return max_count