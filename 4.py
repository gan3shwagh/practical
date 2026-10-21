
class Student:
    def __init__(self, roll, name, marks):
        self.roll = roll
        self.name = name
        self.marks = marks
        self.next = None


class Student_list:
    def __init__(self):
        self.head = None

    def add_student(self, roll, name, marks):
        new = Student(roll, name, marks)
        if not self.head:
            self.head = new
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new
        print("Student added successfully.")

    def print(self):
        cur = self.head
        if not cur:
            print("No records available.")
        while cur:
            print("Roll no.:", cur.roll)
            print("Name:", cur.name)
            print("Marks:", cur.marks)
            cur = cur.next

    def delete(self, roll):
        cur, prev = self.head, None
        while cur:
            if cur.roll == roll:
                if prev:
                    prev.next = cur.next
                else:
                    self.head = cur.next
                print("Student deleted successfully.")
                return
            prev, cur = cur, cur.next
        print("Record not found.")

    def update(self, roll, name, marks):
        cur = self.head
        while cur:
            if cur.roll == roll:
                cur.name, cur.marks = name, marks
                print("Student updated successfully.")
                return
            cur = cur.next
        print("Record not found.")

    def search(self, roll):
        cur = self.head
        while cur:
            if cur.roll == roll:
                print("Record found:", cur.roll, cur.name, cur.marks)
                return
            cur = cur.next
        print("Record not found.")

    def sort(self, key="roll", ascending=True):
        students = []
        cur = self.head
        while cur:
            students.append((cur.roll, cur.name, cur.marks))
            cur = cur.next

        if key == "roll":
            students.sort(key=lambda x: x[0], reverse=not ascending)
        elif key == "marks":
            students.sort(key=lambda x: x[2], reverse=not ascending)
        else:
            print("Invalid sort key.")
            return

        for s in students:
            print(f"Roll: {s[0]}, Name: {s[1]}, Marks: {s[2]}")

    def menu(self):
        while True:
            print("\n1.Add  2.Update  3.Search  4.Delete")
            print("5.Print  6.Sort  7.Exit")
            choice = input("Enter choice: ")

            if choice == '1':
                self.add_student(int(input("Roll: ")),
                                 input("Name: "),
                                 float(input("Marks: ")))
            elif choice == '2':
                self.update(int(input("Roll: ")),
                            input("New name: "),
                            float(input("New marks: ")))
            elif choice == '3':
                self.search(int(input("Roll: ")))
            elif choice == '4':
                self.delete(int(input("Roll: ")))
            elif choice == '5':
                self.print()
            elif choice == '6':
                key = input("Sort by 'roll' or 'marks': ").strip().lower()
                order = input("Ascending or descending: ").strip().lower()
                self.sort(key, order == "ascending")
            elif choice == '7':
                print("Exited.")
                break
            else:
                print("Invalid choice!")


stu = Student_list()
stu.menu()
