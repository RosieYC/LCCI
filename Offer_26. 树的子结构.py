# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if A==None and B == None:
            return True 
        if A==None or B==None:
            return False
        def dfs(Node1, Node2):
            if Node2 ==None:
                return True 
            if Node1 ==None:
                return False 
            if Node1.val != Node2.val :
                return False
            if Node1.val == Node2.val:
                return dfs(Node1.left, Node2.left) and dfs(Node1.right, Node2.right)
       
        return dfs(A,B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)
