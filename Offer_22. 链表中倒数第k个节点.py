# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        P = head
        N_2 = head  
        for i in range(k):
            N_2 = N_2.next
        while (N_2!=None):
            P = P.next 
            N_2 = N_2.next 
        return P
