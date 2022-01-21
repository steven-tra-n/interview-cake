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

    # nodes = []
    # nodes.append(root)

    # while nodes:
    #     current = nodes.pop()
    #     left = current.left
    #     right = current.right

    #     if (left and left.value > current.value) or (right and right.value < current.value):
    #         return False
        
    #     if left and (left.left or left.right):
    #         nodes.append(left)
    #     if right and (right.left or right.right):
    #         nodes.append(right)

    # End BFS solution

    # 0. If root is empty, it is technically a binary search tree
    # 1. Start with an arbitraily upper and lower bound
    # 2. Traverse the tree, DFS
    # 3. If the node value is lower than the lower bound or higher than upper bound, return false
    # 4. If the node has children, append them

    # 0.
    if not root:
        return True

    # 1.
    nodes_and_bounds = [(root, -float('inf'), float('inf'))]

    while nodes_and_bounds:
        node, lower_bound, upper_bound = nodes_and_bounds.pop()

        if node.value <= lower_bound or node.value >= upper_bound:
            return False

        if node.left:
            nodes_and_bounds.append((node.left, lower_bound, node.value))
        if node.right:
            nodes_and_bounds.append((node.right, node.value, upper_bound))

    return True

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

print(binary_search_tree(root))