def invertBinary(root):
    if not root:
        return None
    tmp = root.left
    root.left = root.right
    root.right = tmp

    invertBinary(root.left)
    invertBinary(root.right)
    return root