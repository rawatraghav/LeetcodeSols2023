
# https://leetcode.com/problems/find-pivot-index/description/?envType=study-plan-v2&envId=leetcode-75

# Optimized Solution
# https://leetcode.com/problems/find-pivot-index/solutions/2470014/very-easy-100-fully-explained-java-c-python-js-python3/?envType=study-plan-v2&envId=leetcode-75
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        S = sum(nums)
        leftsum = 0
        for i, x in enumerate(nums):
            if leftsum == (S - leftsum - x):
                return i
            leftsum += x
        return -1


# My solution         

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        summ = sum(nums)
        length = len(nums)
        i = 0

        while i < length:
            sum_left = sum(nums[:i])
            if sum_left == summ - sum_left - nums[i]:
                return i
            i += 1
    
        return -1
    

