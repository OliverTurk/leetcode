# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        children = defaultdict(lambda: [None, None])
        child_nodes = set()

        root = None

        for i, j, k in descriptions:
            if k:
                children[i][0] = j
            else:
                children[i][1] = j

            child_nodes.add(j)
            
        
        for i, j, k in descriptions:
            if i not in child_nodes:
                root = i
                break
        
        def build(parent):
            if not parent:
                return None

            node = TreeNode()

            node.val = parent

            node.left = build(children[parent][0])
            node.right = build(children[parent][1])

            return node

        return build(root)
