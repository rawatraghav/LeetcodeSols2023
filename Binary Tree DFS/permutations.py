
# https://leetcode.com/problems/permutations/description/

# Best Solution

# https://leetcode.com/problems/permutations/solutions/3850900/c-python3-java-easy-explanation-with-image-backtracking-solution/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []


        def recurr(nums, i):
            if len(nums) == i:
                res.append(nums[:])
        
            for j in range(i, len(nums)):
                nums[i], nums[j] = nums[j], nums[i]
                recurr(nums, i+1)
                nums[i], nums[j] = nums[j], nums[i]
        
        recurr(nums, 0)

        return res