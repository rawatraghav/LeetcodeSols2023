
# https://leetcode.com/problems/validate-binary-search-tree/description/

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # Helper function to recursively check node value against a range
        def helper(node, low=float('-inf'), high=float('inf')):
            if not node:
                return True
            if not low < node.val < high:
                return False
            # Recursively check left (with updated high) and right (with updated low)
            return helper(node.left, low, node.val) and helper(node.right, node.val, high)

        return helper(root)
        