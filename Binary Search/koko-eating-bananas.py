
# https://leetcode.com/problems/koko-eating-bananas/description/

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        """
        Very interesting. We need a search space and need to search for a maximum number to eat all piles in h hours. Instead of searching the range from small to large values, we perform a binary search for potential k
        """

        l, r = 1, max(piles)
        res = r

        while l<=r:
            k = (l+r)//2
            hours = 0
            for p in piles:
                hours += math.ceil(p/k)
            
            if hours <= h:
                res = min(res, k)
                r = k-1
            else:
                l = k+1

        return res