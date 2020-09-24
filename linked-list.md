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

# reversing a linked list (source: https://www.youtube.com/watch?v=O0By4Zq0OFc&ab_channel=BackToBackSWE)

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

# doubly linked list
- LinkedList has access to both First and Last
- each node has access to both next and prev

## additional basic operations
- insert last
- delete last
- insert after
- display forward
- display backward

## implementations
- https://www.tutorialspoint.com/difference-between-singly-linked-list-and-doubly-linked-list-in-java#:~:text=Singly%20linked%20list%20allows%20traversal,allows%20element%20two%20way%20traversal.&text=As%20singly%20linked%20list%20store,per%20node(two%20pointers).
- https://www.youtube.com/watch?v=ZlNKNSz88Nk&ab_channel=BlueTreeCode
