class LinearProbingHash:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return key % self.size

    def insert(self, key):
        index = self.hash_function(key)
        for i in range(self.size):
            new_index = (index + i) % self.size
            if self.table[new_index] is None or self.table[new_index] == "<DELETE>":
                self.table[new_index] = key
                print(f"{key} inserted at index {new_index}")
                return
        print("Hash table is full")

    def search(self, key):
        index = self.hash_function(key)
        for i in range(self.size):
            new_index = (index + i) % self.size
            if self.table[new_index] == key:
                print(f"Key {key} found at index {new_index}")
                return new_index
            if self.table[new_index] is None:
                break
        print("Key not found")
        return -1

    def delete(self, key):
        index = self.hash_function(key)
        for i in range(self.size):
            new_index = (index + i) % self.size
            if self.table[new_index] == key:
                self.table[new_index] = "<DELETE>"
                print(f"Key {key} deleted")
                return True
            if self.table[new_index] is None:
                break
        print("Key not found")
        return False

    def display(self):
        for i, val in enumerate(self.table):
            print(f"Index {i}: {val}")

def menu():
    h = LinearProbingHash(10)
    while True:
        print("\n1. Display Table")
        print("2. Insert")
        print("3. Search")
        print("4. Delete")
        print("5. Exit")
        ch = int(input("Enter Your Choice:-"))
        if ch == 1:
            h.display()
        elif ch == 2:
            key = int(input("Enter Key to Insert:"))
            h.insert(key)
        elif ch == 3:
            key = int(input("Enter Key to Search:"))
            h.search(key)
        elif ch == 4:
            key = int(input("Enter Key to Delete:"))
            h.delete(key)
        elif ch == 5:
            print("Exiting...")
            return
        else:
            print("Invalid Choice")

menu()
