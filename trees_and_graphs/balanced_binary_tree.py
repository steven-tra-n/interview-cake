import BinaryTreeNode

def balanced_binary_tree(root):
    # 1. If root is empty, then tree is superbalanced
    # 2. Store an array holding unique depth levels of the tree
    # 3. Store nodes as tuples of node, depth
    # 4. Traverse the tree
    # 5. Pop a node out
    # 6. Once a leaf is hit, append it to depths if it is unique
    # 7. If there are more than 2 different unique depths, the tree is unbalanced
    # 8. If the difference between any two leaf depths are greater than 1, the tree is unbalanced
    # 9. Keep traversing the tree

    # 1.
    if root is None:
        return True

    # 2.
    depths = []

    # 3.
    nodes = []

    # Initialize depth to 0
    nodes.append((root, 0))

    # 2.
    while(nodes):
        node, depth = nodes.pop()

        # Leaf reached
        if (not node.left) and (not node.right):

            # 6.
            if depth not in depths:
                depths.append(depth)

                # 7. and 8.
                if((len(depths) > 2) or (len(depths) == 2) and abs(depths[0] - depths[1]) > 1):
                    return False
        else: # 9.
            depth_increment = depth + 1

            if node.left:
                nodes.append((node.left, depth_increment))
            if node.right:
                nodes.append((node.right, depth_increment))

    return True

root = BinaryTreeNode.BinaryTreeNode(1)
root.insert_left(2)
root.insert_right(3)

print(balanced_binary_tree(root))