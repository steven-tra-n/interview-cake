import LinkedListNode

def has_cycle(head):
    # 1.  Have two pointers to traverse the linked list. One slow, one fast
    # 2.  If they ever intersect, the linked list has a cycle

    fast = head
    slow = head
    
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if fast == slow:
            return True

    return False

head = LinkedListNode.LinkedListNode(1)
head.next = LinkedListNode.LinkedListNode(2)
head.next.next = LinkedListNode.LinkedListNode(3)
head.next.next.next = head

print(has_cycle(head))