# first way to create a tree
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.left.left.left = Node(8)

# second way to create a tree
def create_tree(root, arr):
    if len(arr) == 0:
        return
    root.val = arr[0]
    root.left = Node(arr[1])
    root.right = Node(arr[2])
    create_tree(root.left, arr[3:])
    create_tree(root.right, arr[3:])
    return root