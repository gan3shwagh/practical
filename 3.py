class TextEditor:
    def __init__(self):
        self.state = ""
        self.undo_stack = []
        self.redo_stack = []

    def make_change(self, new_state):
        self.undo_stack.append(self.state)
        self.state = new_state
        self.redo_stack.clear()

    def undo(self):
        if self.undo_stack:
            self.redo_stack.append(self.state)
            self.state = self.undo_stack.pop()
        else:
            print("Nothing to undo")

    def redo(self):
        if self.redo_stack:
            self.undo_stack.append(self.state)
            self.state = self.redo_stack.pop()
        else:
            print("Nothing to redo")

    def show_state(self):
        print("Current state:", self.state)

def menu(editor):
    print("\n1. Make Change")
    print("2. Undo")
    print("3. Redo")
    print("4. Show State")
    print("5. Exit")
    choice = input("Enter choice:")
    if choice == "1":
        new_state = input("Enter new state:")
        editor.make_change(new_state)
    elif choice == "2":
        editor.undo()
    elif choice == "3":
        editor.redo()
    elif choice == "4":
        editor.show_state()
    elif choice == "5":
        return
    else:
        print("Invalid choice")
    menu(editor)

if __name__ == "__main__":
    editor = TextEditor()
    menu(editor)
