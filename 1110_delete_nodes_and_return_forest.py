class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        res = []
        to_delete = set(to_delete)

        def dfs(node):
            if not node:
                return None

            node.left = dfs(node.left)
            node.right = dfs(node.right)

            if node.val in to_delete:
                if node.left:
                    res.append(node.left)
                if node.right:
                    res.append(node.right)

                return None

            return node

        root = dfs(root)

        if root:
            res.append(root)

        return res
