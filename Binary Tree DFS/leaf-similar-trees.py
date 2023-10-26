
# https://leetcode.com/problems/leaf-similar-trees/description/?envType=study-plan-v2&envId=leetcode-75

# Best Solution 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
    
        def getOrder(root):

            if root == None:
                return []
            
            if not root.left and not root.right:
                return [root.val]

            return getOrder(root.left) + getOrder(root.right)
        
        order1 = getOrder(root1)
        order2 = getOrder(root2)

        return order1 == order2

        