# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None:
            return 
        if head.next == None:
            return head 
        P = None
        cur = head 
        while(cur):
            N = cur.next 
            cur.next = P
            P = cur 
            cur = N 
        return P
