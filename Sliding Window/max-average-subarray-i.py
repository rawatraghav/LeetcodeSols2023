
# https://leetcode.com/problems/maximum-average-subarray-i/description/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        length = len(nums)
        next_sum = sum(nums[:k])
        max_avg = next_sum/k

        for i in range(k, length):
            next_sum = next_sum - nums[i-k] + nums[i]
            temp = next_sum/k
            max_avg = max(temp, max_avg)
        
        return max_avg