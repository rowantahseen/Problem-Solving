'''
This is a Top Down approach for tree traversal PreOrder Traversal :
1. Think of similarly to the "get all elements in the same tree level problem"
2. We also need to keep track of Parent node, in order to make sure the 2 nodes don't have the same parent
3. I used a Nested Disctionary structure almost similiar to the json format to be easily accessed which is
{level : {node_value : parent_node_value}
example:	
				{0: {1: None}, 
				 1: {2: 1, 3: 1},
				 2: {4: 2}}	 
4. True if x and y are both in the same level and that their paren_node_value are different, otherwise False
'''
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        levels = {}
        
        def traverse(node, parent , level):
            if not node:
                return
            levels[level] = levels.get(level,{})
            levels[level].update({node.val:parent})
            traverse(node.left, node.val, level+1)
            traverse(node.right, node.val, level+1)
            
        traverse(root,None,0)
        
        for l in levels:
            if x in levels[l] and y in levels[l]:
                if levels[l][x] != levels[l][y]:
                    return True
        return False
