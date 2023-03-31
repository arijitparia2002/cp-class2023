# 129. Sum Root to Leaf Numbers
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        def DFS(root, currVal):
            if root == None:
                return
            if root.right == None and root.left==None:
                self.ans += (currVal*10 + root.val)

            DFS(root.right, currVal*10 + root.val)
            DFS(root.left, currVal*10 + root.val)

        self.ans = 0
        DFS(root, 0)
        return self.ans
    
########################################################################################################

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        def DFS(root, currVal):
            if root == None:
                return
            DFS(root.right, currVal*10 + root.val)
            
            if root.right == None and root.left==None:
                self.ans += (currVal*10 + root.val)

            DFS(root.left, currVal*10 + root.val)

        self.ans = 0
        DFS(root, 0)
        return self.ans
            
            


            

            
            


            
