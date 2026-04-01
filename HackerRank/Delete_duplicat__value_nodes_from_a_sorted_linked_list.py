def removeDuplicates(llist):
    curr=llist
    while curr and curr.next:
        if curr.data==curr.next.data:
            curr.next=curr.next.next
        else:
            curr=curr.next
    return llist
