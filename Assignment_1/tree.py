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
def create_tree(arr, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    root = Node(arr[mid])
    root.left = create_tree(arr, start, mid-1)
    root.right = create_tree(arr, mid+1, end)
    return root
create_tree ([1, 5, 3, 19, 18, 25], 0, 5)