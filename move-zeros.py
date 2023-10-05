
# https://leetcode.com/problems/move-zeroes/

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count=nums.count(0)
        nums[:]=[i for i in nums if i != 0]
        nums+=[0]*count
            
        return nums


# NOTE
# We used nums[:] to perform in place operation in the memory
# using just nums would have assigned new memory space