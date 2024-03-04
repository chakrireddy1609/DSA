def removeElement(head,val):
    dummy = ListNode(next=head)
    prev,curr = dummy,head
    while curr:
        nxt = curr.next
        if curr.val == val:
            prev = nxt
        else:
            prev = curr
        curr = nxt
    return dummy.next
