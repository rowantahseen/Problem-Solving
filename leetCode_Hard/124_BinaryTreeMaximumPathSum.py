# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        result = [float('-inf')]
        
        def max_(node):
            if node:
                left = max_(node.left)
                right = max_(node.right)
                left_path = left+node.val
                right_path = right+node.val
                both_paths = left+right+node.val
                result[0] = max(result[0],node.val,left_path,right_path,both_paths)
                return max(left_path,right_path,node.val)
            return 0
        
        max_(root)
        return result[0]
