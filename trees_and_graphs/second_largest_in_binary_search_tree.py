import BinaryTreeNode

def second_largest_in_binary_search_tree(root):
    # 0. Root is empty
    # 1. Node has a right child so we did not find the max yet. Keep traversing
    # 2. Store previous value
    # 3. Node has a left child and that left child has a right child so we did not find the max yet. Keep traversing
    # 4. Node has a left child and that left child does not have a right child. Second highest found

    if not root:
        return False

    nodes = []
    nodes.append(root)

    while nodes:
        node = nodes.pop()

        # 1.
        if node.right:
            nodes.append(node.right)
            # 2.
            previous_value = node.value
        elif node.left and node.left.right: # 3.
            nodes.append(node.left)
        elif node.left and not node.left.right:
            return node.value
        else:
            return previous_value
    
    print('hello')

root = BinaryTreeNode.BinaryTreeNode(50)
root.insert_left(17)
root.left.insert_left(12)
root.left.left.insert_left(9)
root.left.left.insert_right(14)
root.left.insert_right(23)
root.left.right.insert_left(19)
root.insert_right(72)
root.right.insert_left(54)
root.right.left.insert_right(67)
root.right.insert_right(76)

print(second_largest_in_binary_search_tree(root))