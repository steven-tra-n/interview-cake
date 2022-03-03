from turtle import pos
import LinkedListNode

def kth_last_node(head, position):
    # 1.  Iterate through the entire list, keeping a counter variable for length
    # 2.  Reset current, traverse again until position

    # current = head
    # counter = 0

    # while current is not None:
    #     current = current.next
    #     counter += 1

    # current = head

    # while current is not None and counter > position:
    #     current = current.next
    #     counter -= 1

    # return current

    # End double iteration

    # 1.  Create two pointers, seperated by position distance
    # 2.  Move both pointers along, until the end is reached
    # 3.  Return the first pointer

    start = head
    end = head

    # 1.
    while end and position > 0:
        end = end.next
        position -= 1

    # 2.
    while end:
        start = start.next
        end = end.next

    # 3.
    print(start.value)

head = LinkedListNode.LinkedListNode(1)
head.next = LinkedListNode.LinkedListNode(2)
head.next.next = LinkedListNode.LinkedListNode(3)
head.next.next.next = LinkedListNode.LinkedListNode(4)
head.next.next.next.next = LinkedListNode.LinkedListNode(5)

kth_last_node(head, 1)