from lab_7class import BTNode

def find_LCA(root, x, y):
    if root is None:
        return None

    # If both x and y are smaller than root, then LCA lies in left
    if x < root.elem and y < root.elem:
        return find_LCA(root.left, x, y)

    # If both x and y are greater than root, then LCA lies in right
    if x > root.elem and y > root.elem:
        return find_LCA(root.right, x, y)

    # If one key is on one side and the other is on the other side, this root is the LCA
    return root

# Now let's build the tree from the image
root = BTNode(15)
root.left = BTNode(10)
root.right = BTNode(25)
root.left.left = BTNode(8)
root.left.right = BTNode(12)
root.left.left.left = BTNode(6)
root.left.left.right = BTNode(9)
root.right.left = BTNode(20)
root.right.right = BTNode(30)
root.right.left.left = BTNode(18)
root.right.left.right = BTNode(22)

# Test examples
pairs = [(6, 12), (20, 6), (18, 22), (20, 25), (10, 12)]
for x, y in pairs:
    lca = find_LCA(root, x, y)
    print(f"LCA({x},{y}) = {lca.elem}")
