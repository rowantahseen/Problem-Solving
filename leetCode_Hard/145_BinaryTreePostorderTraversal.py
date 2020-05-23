# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
    
    '''
    Recursive Approach
    '''
    
#         def dfs(root,out):
#             if root is None:
#                 return out
#             print(root.val)
#             dfs(root.left,out)
#             dfs(root.right,out)
#             out.append(root.val)

        
#         out=[]
#         dfs(root,out)
#         return out

    '''
    Iteritave Approach
    '''
    
        out=[]
        stack = [root]
        while stack:
            current = stack.pop()
            if current:
                out.append(current.val)
                if current.left:
                    stack.append(current.left)
                if current.right:
                    stack.append(current.right)
        return out[::-1]
    
