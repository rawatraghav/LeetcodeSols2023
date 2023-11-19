
# https://leetcode.com/problems/longest-consecutive-sequence/


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0

        nums = set(nums)

        longest = 0
        length = 0

        for num in nums:
            
            if num-1 not in nums:
                length = 1
                while num+length in nums:
                    length += 1
                longest = max(longest, length)
        
        return longest
            