class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp_head = head 
        #### count total length ####
        count = 0 
        while temp_head:
            if temp_head.val!=None:
                count +=1 
                temp_head = temp_head.next
        #### cut cut_num th ####
        cut_num = count - n  
        pre = ListNode(None) 
        pre.next = head 
        #### except 
        if cut_num == 0:
            pre.next = head.next
            return pre.next
        #### normal 
        temp_head = head 
        while cut_num>0:
            cut_num -= 1
            if cut_num == 0:
                temp_head.next = temp_head.next.next
                return head 
            temp_head = temp_head.next
