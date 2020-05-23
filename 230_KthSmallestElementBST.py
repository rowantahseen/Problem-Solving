class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        out = []
        def dfs(node):
            if node == None:
                return
            dfs(node.left)
            out.append(node.val)
            dfs(node.right)
                
            
        dfs(root)    
        return out[k-1]
