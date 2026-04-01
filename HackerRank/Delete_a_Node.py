def deleteNode(llist, position):
    curr=llist
    if llist is None:
        return None
    if position == 0:
        return llist.next
    for _ in range(position-1):
        curr=curr.next
    curr.next=curr.next.next  
    
    return llist    
        
