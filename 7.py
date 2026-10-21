class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert(self.root, data)

    def _insert(self, root, data):
        if root is None:
            return Node(data)
        if data < root.data:
            root.left = self._insert(root.left, data)
        else:
            root.right = self._insert(root.right, data)
        return root

    def search(self, key):
        current = self.root
        while current:
            if key == current.data:
                print("Found")
                return True
            elif key < current.data:
                current = current.left
            else:
                current = current.right
        print("Not Found")
        return False

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, root, key):
        if root is None:
            return root
        if key < root.data:
            root.left = self._delete(root.left, key)
        elif key > root.data:
            root.right = self._delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            temp = self._min_value_node(root.right)
            root.data = temp.data
            root.right = self._delete(root.right, temp.data)
        return root

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder(self):
        self._inorder(self.root)
        print()

    def _inorder(self, root):
        if root:
            self._inorder(root.left)
            print(root.data, end=" ")
            self._inorder(root.right)

    def preorder(self):
        self._preorder(self.root)
        print()

    def _preorder(self, root):
        if root:
            print(root.data, end=" ")
            self._preorder(root.left)
            self._preorder(root.right)

def menu():
    b = BST()
    while True:
        print("\n1. Insert")
        print("2. Search")
        print("3. Delete")
        print("4. Inorder Traversal")
        print("5. Preorder Traversal")
        print("6. Exit")
        ch = int(input("Enter Choice:"))
        if ch == 1:
            val = int(input("Enter Value:"))
            b.insert(val)
        elif ch == 2:
            val = int(input("Enter Value to Search:"))
            b.search(val)
        elif ch == 3:
            val = int(input("Enter Value to Delete:"))
            b.delete(val)
        elif ch == 4:
            b.inorder()
        elif ch == 5:
            b.preorder()
        elif ch == 6:
            break
        else:
            print("Invalid Choice")

menu()
