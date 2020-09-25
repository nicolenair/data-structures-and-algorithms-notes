#iterative
def reverseList(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    current = head
    l_prev = []
    prev = None
    while current!=None:
        next = current.next #original next
        current.next = prev #set my next to the previous
        prev = current #set previous to current
        current = next #move to next node
    return prev
    
#recursive  
def reverseList(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    #base case
    if head==None or head.next==None:
        return head
    #traverse down
    rlh = Solution.reverseList(self, head.next)
    #traverse up
    head.next.next = head
    head.next = None
    return rlh
