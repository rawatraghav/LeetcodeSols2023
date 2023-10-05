# https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maximum = 0
        
        while left != right:
            l = right - left
            b = min(height[right],height[left])
            area = l*b
            maximum = max(maximum,area)
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return maximum