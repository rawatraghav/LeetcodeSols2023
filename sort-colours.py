# https://leetcode.com/problems/sort-colors/submissions/



class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # SOL 1
        # for i in range(len(nums)):
        #     for j in range(len(nums)-i-1):
        #         if nums[j]>nums[j+1]:
        #             nums[j], nums[j+1] = nums[j+1], nums[j]
        
        # SOL 2
        # cnt = Counter(nums)
        # nums[:] = cnt[0]*[0] + cnt[1]*[1] + cnt[2]*[2]
        # print(cnt)             