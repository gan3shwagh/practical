class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def build_expression_tree(prefix_expr):
    stack = []
    for char in reversed(prefix_expr):
        node = Node(char)
        if char in "+-*/":
            if stack:
                node.left = stack.pop()
            if stack:
                node.right = stack.pop()
        stack.append(node)
    return stack[0] if stack else None

def non_recursive_postorder(root):
    if root is None:
        return
    stack1 = []
    stack2 = []
    stack1.append(root)
    while stack1:
        node = stack1.pop()
        stack2.append(node)
        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)
    while stack2:
        print(stack2.pop().data, end=" ")
    print()

def delete_tree(root):
    if root:
        delete_tree(root.left)
        delete_tree(root.right)
        del root

def menu():
    expr = input("Enter Prefix Expression (e.g., +-*ab/cd): ")
    root = build_expression_tree(expr)
    print("Post-order Traversal:")
    non_recursive_postorder(root)
    delete_tree(root)
    print("Tree Deleted")

menu()
