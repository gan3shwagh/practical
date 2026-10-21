class ChainingHashing:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return key % self.size

    def Insert(self, key):
        index = self.hash_function(key)
        if key not in self.table[index]:
            self.table[index].append(key)
            print(f"{key} inserted at index{index}")
        else:
            print(f"{key} already exists")

    def search(self, key):
        index = self.hash_function(key)
        if key in self.table[index]:
            return index
        return -1

    def delete(self, key):
        index = self.hash_function(key)
        if key in self.table[index]:
            self.table[index].remove(key)
            return True
        return False

    def display(self):
        for i, bucket in enumerate(self.table):
            print(f"Index{i}:{bucket}")

    def menu(self):
        while True:
            print("\n1. Display Table")
            print("2. Insert In Table")
            print("3. Search In Table")
            print("4. Delete In Table")
            print("5. Exit")
            ch = int(input("Enter Your Choice:-"))
            if ch == 1:
                self.display()
            elif ch == 2:
                key = int(input("Enter A Number You Want To Insert:"))
                self.Insert(key)
            elif ch == 3:
                key = int(input("Enter Element You Want To Search:"))
                index = self.search(key)
                if index != -1:
                    print(f"Key Found at Index{index}")
                else:
                    print("Key Not Found")
            elif ch == 4:
                key = int(input("Enter Element You Want To Delete:"))
                if self.delete(key):
                    print(f"{key} deleted")
                else:
                    print("Key Not Found")
            elif ch == 5:
                print("Exiting...")
                return
            else:
                print("Enter Valid Choice")

Ch = ChainingHashing(10)
Ch.menu()
