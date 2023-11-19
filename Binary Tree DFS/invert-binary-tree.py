

# https://leetcode.com/problems/invert-binary-tree/description/

# Time complexity O(N)
# Space Complexity O(N)

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root:
            return None

        def dfs(root):

            if not root:
                return 

            dfs(root.left)
            dfs(root.right)
            root.right, root.left = root.left, root.right

            return
        
        dfs(root)

        return root