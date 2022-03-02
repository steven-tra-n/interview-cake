import LinkedListNode

def delete_node(node):
    # 1.  Replace the current node with next node

    next = node.next

    if next:
        node.value = next.value
        node.next = next.next
    else:
        raise Exception('Cannot delete the last node')


a = LinkedListNode('A')
b = LinkedListNode('B')
c = LinkedListNode('C')

a.next = b
b.next = c

delete_node(b)
print(a)
print(b)
print(c)