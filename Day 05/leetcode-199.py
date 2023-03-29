# 199. Binary Tree Right Side View

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        queue = [root]
        next_queue = []
        result = []
        level = []

        while queue:
            for root in queue:
                level.append(root.val)
                if(root.left):
                    next_queue.append(root.left)
                if(root.right):
                    next_queue.append(root.right)

            print(level)
            result.append(level[-1])
            queue = next_queue
            level = []
            next_queue = []
        return result
