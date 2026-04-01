def insertNodeAtPosition(llist, data, position):
    node=SinglyLinkedListNode(data)
    if position ==0:
        llist=node
        
    curr=llist
    for _ in range(position-1):
        curr=curr.next
    node.next=curr.next
    curr.next=node
    
    return llist   
