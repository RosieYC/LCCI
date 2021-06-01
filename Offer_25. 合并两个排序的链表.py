# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        pre = ListNode(-1)
        head = pre 
        pre.next = l1 
        if l1 == None :
            return l2 
        if l2 == None:
            return l1
        while l1 != None :
            if l1.val >= l2.val:
                if l2.next != None:
                    N = l2.next 
                    l2.next = l1 
                    pre.next = l2 
                    pre = l2 
                    l2 = N 
                else:
                    l2.next = l1 
                    pre.next = l2 
                    break
            else:
                if l1.next == None:
                    l1.next = l2 
                    break
                else:
                    pre = l1
                    l1 = l1.next 
        return head.next
