def compare_lists(llist1, llist2):
    curr1=llist1
    curr2=llist2
    while curr1 and curr2 and curr1.next and curr2.next:
        if curr1.data!=curr2.data:
            return 0
        curr1=curr1.next
        curr2=curr2.next
    if curr1.next or curr2.next:
        return 0
    return 1
