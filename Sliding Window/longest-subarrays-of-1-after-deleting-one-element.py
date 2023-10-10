
# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/description/?envType=study-plan-v2&envId=leetcode-75

# best solution 
# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/solutions/3719568/beat-s-100-c-java-python-beginner-friendly/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        left = right = 0
        length = len(nums)
        zeros = 0
        max_res = 0

        while right < length:

            if nums[right] == 0:
                zeros += 1
            
            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
                
            max_res = max(right-left, max_res)
            right += 1
        
        return max_res