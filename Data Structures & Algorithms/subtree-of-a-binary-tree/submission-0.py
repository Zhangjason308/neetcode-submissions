# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSametree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Essentially like the same tree, except now subroot)
        if root is None and subRoot is None:
            return True
        elif root is None or subRoot is None:
            return False
        else:
            if subRoot.val != root.val:
                return False
            return self.isSametree(root.left, subRoot.left) and self.isSametree(root.right, subRoot.right)
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot is None:
            return True
        if root is None:
            return False
        if self.isSametree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)






