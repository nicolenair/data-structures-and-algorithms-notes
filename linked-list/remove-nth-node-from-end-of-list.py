# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        curr = head
        llist = 1
        while curr.next!=None:
            curr = curr.next
            llist+=1
        node_to_delete = llist-n
        
        curr = head
        
        if curr.next==None:
            head = None
            return head
        
        elif node_to_delete==0:
            curr = head.next
            head.next = None
            return curr
        
        for i in range(node_to_delete-1):
            curr = curr.next
        
        print(curr)
        if curr.next.next!=None:
            next_next = curr.next.next
            curr.next.next = None
            curr.next = next_next
            
        else:
            curr.next=None
        return head
            
#one pass?
"""
"""
            
            
            
            
        
