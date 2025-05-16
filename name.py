class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def build_balanced_bst(self, sorted_keys):
        self.root = self._build_balanced_bst_helper(sorted_keys, 0, len(sorted_keys) - 1)

    def _build_balanced_bst_helper(self, arr, start, end):
        if start > end:
            return None
        mid = (start + end) // 2
        node = Node(arr[mid])
        node.left = self._build_balanced_bst_helper(arr, start, mid - 1)
        node.right = self._build_balanced_bst_helper(arr, mid + 1, end)
        return node

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.key, end=" ")
            self.inorder(node.right)


bst = BinarySearchTree()

sorted_keys = [4, 7, 8, 11, 12, 13, 14, 16, 17, 19, 20, 53, 60]
bst.build_balanced_bst(sorted_keys)

print("In-order traversal of balanced BST:")
bst.inorder(bst.root)
print()
