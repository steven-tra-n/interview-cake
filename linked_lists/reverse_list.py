import LinkedListNode

def reverse_list(head):
    # 1.  Initialize previous node to null
    # 2.  Temporarily store next
    # 3.  Make current point to previous
    # 4.  Advance previous to current
    # 5.  Advance next

    prev = None
    current = head

    while current is not None:
        next = current.next
        current.next = prev
        prev = current
        current = next

    return prev

head = LinkedListNode.LinkedListNode(1)
head.next = LinkedListNode.LinkedListNode(2)
head.next.next = LinkedListNode.LinkedListNode(3)
head.next.next.next = LinkedListNode.LinkedListNode(4)

reverse_list(head)