class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = []

        best = -inf
        res = 0

        queue.append(root)
        level = 1

        while queue:
            next_level = []
            level_sum = 0
        
            while queue:
                node = queue.pop()
                level_sum += node.val
    
                if node.left:
                    next_level.append(node.left)
                
                if node.right:
                    next_level.append(node.right)

            queue += next_level

            if level_sum > best:
                best = level_sum
                res = level

            level += 1

        return res
