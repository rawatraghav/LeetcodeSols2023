

# https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/description/


# Best Solution
# https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/solutions/940618/python3-dfs-o-n/ 
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        
        @lru_cache(None)
        def fn(node):
            """Return height of tree rooted at node."""
            if not node: return 0
            return 1 + max(fn(node.left), fn(node.right))
        
        node = root
        while node: 
            left, right = fn(node.left), fn(node.right)
            if left == right: return node
            elif left > right: node = node.left
            else: node = node.right     