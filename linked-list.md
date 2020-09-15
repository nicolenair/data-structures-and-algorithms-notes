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
-  locate target node to be removed using a search alg
- leftnode.next = targetnode.next
- targetnode.next = NULL
- you can delete from memory (or not)

# reversing a linked list
- TBA

