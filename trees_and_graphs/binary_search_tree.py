import BinaryTreeNode

def binary_search_tree(root):
    # 1. If tree is empty, then it is not a valid binary search tree
    # 2. Append root into array
    # 3. Loop through array
    # 4. Save current, left, and right values
    # 5. BFS
    # 6. If at any point left is greater than current or right is less than current, return false
    # 7. Keep traversing
    # 8. Return true

    nodes = []
    nodes.append(root)

    while nodes:
        current = nodes.pop()
        left = current.left
        right = current.right

        if (left and left.value > current.value) or (right and right.value < current.value):
            return False
        
        if left and (left.left or left.right):
            nodes.append(left)
        if right and (right.left or right.right):
            nodes.append(right)

    return True

root = BinaryTreeNode.BinaryTreeNode(50)
root.insert_left(17)
root.left.insert_left(12)
root.left.left.insert_left(9)
root.left.left.insert_right(14)
root.left.insert_right(23)
root.left.right.insert_left(19)
root.insert_right(49)
root.right.insert_left(54)
root.right.left.insert_right(67)
root.right.insert_right(76)

print(binary_search_tree(root))