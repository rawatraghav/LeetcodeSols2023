

# https://leetcode.com/problems/removing-stars-from-a-string/description/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def removeStars(self, s: str) -> str:
        
        res = []

        for ch in s:
            if ch != '*':
                res.append(ch)
            else:
                res.pop()

        return ''.join(res)