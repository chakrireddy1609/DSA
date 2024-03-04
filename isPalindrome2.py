def isPalindrome(head):
    slow,fast = head,head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    prev = None
    while slow:
        tmp = slow.next
        slow.next = prev
        prev = slow
        slow = tmp

    left,right = head,prev
    while right:
        if left.val != right.val:
            return False
        left = left.next
        right = right.next
    return True
