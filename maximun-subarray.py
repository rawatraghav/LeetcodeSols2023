# Dynamic Programming, Kadane's Algorithm

# Whenever you see a question that asks for the maximum or minimum of something, consider Dynamic Programming as a possibility.

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        m, max_subarr =  nums[0], nums[0]
        
        for num in nums[1:]:
            max_subarr = max(max_subarr + num,num)
            m = max(max_subarr,m)
        return m