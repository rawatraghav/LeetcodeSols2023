
# https://leetcode.com/problems/find-the-highest-altitude/description/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        presum = 0
        highest = float('-inf')
        
        for num in gain:
            presum += num
            highest = max(highest, presum)
        
        return max(highest, 0)