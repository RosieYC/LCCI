# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        from collections import deque
        if root == None:
            return []
        i = 0 
        q = deque()
        answer = []
        q.append(root)
        while(len(q)>0):
            temp = q.popleft()
            answer.append(temp.val)
            if temp.left != None:
                q.append(temp.left)
            if temp.right != None:
                q.append(temp.right)
        return answer
            
