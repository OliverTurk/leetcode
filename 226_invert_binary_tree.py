class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(root):
            if not root:
                return None
            
            root.left, root.right = dfs(root.right), dfs(root.left) 

            return root

        dfs(root)

        return root
