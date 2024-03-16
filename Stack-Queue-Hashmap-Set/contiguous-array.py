
# https://leetcode.com/problems/contiguous-array/description/?envType=daily-question&envId=2024-03-16

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        """
        We keep a track of all the count values because if we get to the same count value, it means that we encountered an equal
        number of 0s and 1s in the way. Hence, we calculate its length and update the max. 
        For Ex- 
        Say we have a count of 3. After 5 1s and 5 0s we encounter a count of 3 once again. So this subarray size becomes 10.
        """

        count = 0
        result = 0
        dict_seen = {0: -1}
        for i in range(len(nums)):
            n = nums[i]
            if n == 0:
                count -= 1
            if n == 1:
                count += 1
            
            if count in dict_seen:                       # You have been here before
                result = max(result, i-dict_seen[count]) # Get the furthest distance
            else:                     # You haven't been here before
                dict_seen[count] = i  # Mark it
                
        return result