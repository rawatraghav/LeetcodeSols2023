

# https://leetcode.com/problems/count-good-nodes-in-binary-tree/description/?envType=study-plan-v2&envId=leetcode-75

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        stack = [(root, float('-inf'))]
        count = 0
        while stack:
            node, maxNum = stack.pop()
            if node.val >= maxNum:
                count += 1
            maxNum = max(maxNum, node.val)
            if node.left:
                stack.append((node.left, maxNum))
            if node.right:
                stack.append((node.right, maxNum))

        return count

        