
# https://leetcode.com/problems/max-consecutive-ones-iii/description/?envType=study-plan-v2&envId=leetcode-75

# Best Solution Explanation
# https://leetcode.com/problems/max-consecutive-ones-iii/solutions/719833/python3-sliding-window-with-clear-example-explains-why-the-soln-works/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        left = right = 0
        length = len(nums)

        while right < length:

            if nums[right] == 0:
                k -= 1
            
            if k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1

            right += 1

        return right - left