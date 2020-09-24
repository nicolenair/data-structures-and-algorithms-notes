These notes are based on https://www.tutorialspoint.com/data_structures_algorithms/linked_list_algorithms.htm

- a sequence of data structures, connected by links

# important concepts in linked lists
- link (stores data called an element)
- next (each link has a next)
- linkedlist (connected to link called First)

# types of linked lists
- simple (navigate forward only)
- doubly (navigate backward and forward)
- circular (last to first)

# basic operations
- insertion
- deletion
- display
- search
- delete

# insertion
- find where the node should be inserted
- leftnode.next = newnode
- newnode.next = rightnode

# deletion
- locate target node to be removed using a search alg
- leftnode.next = targetnode.next
- targetnode.next = NULL
- you can delete from memory (or not)

# reversing a linked list

## Iterative Approach [O(N) time O(1) space]
~~~
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
~~~

## Recursive Approach
~~~
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
~~~
        
