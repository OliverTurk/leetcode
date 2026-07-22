class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(node):
            if not node:
                return 0, None
            
            left = dfs(node.left)
            right = dfs(node.right)

            if left[0] > right[0]:
                return left[0] + 1, left[1]
            elif left[0] < right[0]:
                return right[0] + 1, right[1]

            return left[0] + 1, node
        
        return dfs(root)[1]
