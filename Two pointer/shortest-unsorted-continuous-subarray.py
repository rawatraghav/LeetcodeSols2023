
# https://leetcode.com/problems/shortest-unsorted-continuous-subarray/

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:

        """
        'end' is assigned starting from the left to as many times there is a number wrongly occuring in the sequence. Same goes
        for 'start' from the right. 
        """
        
        n = len(nums)
        start, end = -1, -2
        min_val, max_val = float('inf'), float('-inf')
        
        for i in range(n):
            max_val = max(max_val, nums[i])
            min_val = min(min_val, nums[n - 1 - i])
            
            if nums[i] < max_val:
                end = i
            
            if nums[n - 1 - i] > min_val:
                start = n - 1 - i
                
        return end - start + 1