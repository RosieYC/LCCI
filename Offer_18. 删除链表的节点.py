# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        ## method 1 
        pre = ListNode(None)
        here = pre
        pre.next = head 
        t = 0
        while(pre.next != None):
            if pre.next.val == val:
                t = 1
            if t == 1:
                pre.next = pre.next.next 
                t = 0
            pre = pre.next
            if pre == None:
                break
        return here.next
        ## method 2
        '''
        pre = ListNode(None)
        pre.next = head
        d = head 
        next = head.next
        while (d != None ):
            if head.val == val:
                return next 
            elif d.val == val:
                pre.next = next
                return head 
            else:
                pre = d 
                d = next 
                next = next.next
        '''
