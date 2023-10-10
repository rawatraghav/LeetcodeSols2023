# Best solution - consists of two-pointer and dictionary (counter) approach
# https://leetcode.com/problems/max-number-of-k-sum-pairs/solutions/961458/python-c-intuitive-2-pointer-o-nlogn-and-o-n-solution/?envType=study-plan-v2&envId=leetcode-75


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        count = 0
        i, j = 0, len(nums) - 1

        while i < j:
            if nums[i] + nums[j] == k:
                count += 1
                i += 1
                j -= 1
            elif nums[i] + nums[j] < k:
                i += 1
            else:
                j -= 1
        
        return count