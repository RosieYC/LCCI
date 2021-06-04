# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        from collections import deque
        if root == None:
            return []
        i = 0 
        answer = []
        ttt1_list = []
        ttt2_list = [root]
        while len(ttt1_list)!= 0 or len(ttt2_list) !=0:
            temp_answer = []
            ttt1_list =  []
            for i in range(len(ttt2_list)):
                temp_answer.append(ttt2_list[i].val)
                if ttt2_list[i].left != None:
                    ttt1_list.append(ttt2_list[i].left) 
                if ttt2_list[i].right != None:
                    ttt1_list.append(ttt2_list[i].right)
            answer.append(temp_answer)
            ttt2_list = ttt1_list
        return answer
