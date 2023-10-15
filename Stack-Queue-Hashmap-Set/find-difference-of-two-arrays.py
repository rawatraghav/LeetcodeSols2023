
# https://leetcode.com/problems/find-the-difference-of-two-arrays/description/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        
        nums1 = set(nums1)
        nums2 = set(nums2)

        res = []

        res.append(nums1-nums2)
        res.append(nums2-nums1)

        return res