# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Use BFS to access level by level
        # Create a data structure -> array to add a list of lists
        res = []
        if root is None:
            return res
        queue = collections.deque([root])

        while queue:
            inner = []
            for i in range(len(queue)):
                node = queue.popleft()
                inner.append(node)
            for i in inner:
                if i.left:
                    queue.append(i.left)
                if i.right:
                    queue.append(i.right)
            for i in range(len(inner)):
                inner[i] = inner[i].val
            res.append(inner)
        return res
    
