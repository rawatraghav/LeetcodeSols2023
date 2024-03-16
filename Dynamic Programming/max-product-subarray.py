
# https://leetcode.com/problems/maximum-product-subarray/description/

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        This is not a DP problem in first look. But since we are maintaining two numbers curMax and curMin, anyone 
        can be used as the solution depending on maximum.
        """
        res = max(nums)
        curMin, curMax = 1, 1

        for n in nums:
            if n == 0:
                curMin, curMax = 1, 1
                continue
            tmp = curMax * n
            curMax = max(n * curMax, n* curMin, n)
            curMin = min(tmp, n*curMin, n)
            res = max(res, curMax)
        
        return res