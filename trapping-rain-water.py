# https://leetcode.com/problems/trapping-rain-water/submissions/


# O(N^2)
class Solution:
    def trap(self, height: List[int]) -> int:
        
        leftmax = 0
        rightmax = 0
        water = 0
        
        for i in range(1,len(height)-1):
            
            leftmax = max(height[:i])
            rightmax = max(height[i+1:])
            water += max(min(leftmax,rightmax) - height[i],0)
            
        return water


# time O(N)
# space O(N)

