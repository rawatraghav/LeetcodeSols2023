
# https://leetcode.com/problems/subsets/description/

# Neetcode video
# https://www.youtube.com/watch?v=REOH22Xwdkk


# Solution 

"""
Why we use .copy() ??

The code you provided generates all the subsets of a given list of numbers using a depth-first search (DFS) approach. 
However, there's a common issue related to how you handle the subset variable.

The problem lies in the fact that you're appending the reference to the subset list to the res list, 
and then you pop elements from the subset. Since lists in Python are mutable objects, if you append the 
reference to a list and then modify the original list, it will affect the appended reference as well. 
This leads to incorrect results in the final res.

"""

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            # Base case
            if i >= len(nums):
                res.append(subset.copy())  # Make a copy of the subset before appending
                return
            
            # Decision to append ith element
            subset.append(nums[i])
            dfs(i + 1)

            # Decision to NOT append ith element, we have to backtrack
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res