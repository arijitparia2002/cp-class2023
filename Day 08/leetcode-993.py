# 993. Cousins in Binary Tree

# BFS + Hashmap approch

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        if root is None:
            return False

        level = 0
        queue = [root]
        next_q = []
        values = {}

        while queue:
            for node in queue:
                if node.left:
                    next_q.append(node.left)
                    values[node.left.val] = node

                if node.right:
                    next_q.append(node.right)
                    values[node.right.val] = node

            level += 1
            if level>1:
                if x in values and y in values and values[x] != values[y]:
                    return True
            queue = next_q
            next_q = []
            values = {}
        return False
    

    #####################################################################