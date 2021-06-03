# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True
        def detect(root1):
            if root1 == None:
                return None
            root1.left, root1.right = root1.right, root1.left
            detect(root1.left) 
            detect(root1.right)
            return root1
        def check(root1, root2):
            if root1 == None and root2==None:
                return True
            if root1 == None and root2 != None:
                return False
            if root1 != None and root2 == None:
                return False
            if root1.val == root2.val:
                return check(root1.left, root2.left) and check(root1.right, root2.right)
            return False 
        root.left = detect(root.left)
        return check(root.right, root.left)
