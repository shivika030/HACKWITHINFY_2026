def insertNodeAtTail(head, data):
    if head is None:
        return SinglyLinkedListNode(data)
    
    if head.next is None:
        head.next = SinglyLinkedListNode(data)
        
    else:
        insertNodeAtTail(head.next, data) 
    
    return head
