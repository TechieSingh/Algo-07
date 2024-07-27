# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:

        def inroder(node):
            if not node:
                return []
            return inroder(node.left) + [node.val] + inroder(node.right)

        sorted_node=inroder(root)

        def build(left,right):
            if left>right:
                return
            mid= (left+right)//2
            node = TreeNode(sorted_node[mid])
            node.left=build(left,mid-1)
            node.right=build(mid+1,right)
            return node
        
        return build(0, len(sorted_node)-1)
        