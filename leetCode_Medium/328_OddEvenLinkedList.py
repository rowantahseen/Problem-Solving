# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head:
            even = head
            start = even
        else:
            return
        if head.next:
            odd = head.next
            join = odd
        else:
            return start
        
        count=0
        pointer = head.next.next
        
        while pointer:
            if count %2 ==0:
                even.next = pointer
                even = even.next
            else:
                odd.next = pointer
                odd = odd.next
            count+=1
            pointer = pointer.next
            
        odd.next = None
        even.next = join
        
        return start
            
            
        
