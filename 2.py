def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def menu():
    salary = [35, 78, 45, 48, 32, 65, 94, 87]
    print("welcome to sorting technique")
    print(" 1.bubble\n 2.selection\n 3.insertion\n 4.Exit\n")
    choice = int(input("enter choice\n"))
    if choice == 4:
        return 1
    if choice == 1:
        print(bubble_sort(salary))
    if choice == 2:
        print(selection_sort(salary))
    if choice == 3:
        print(insertion_sort(salary))
    print("top three salary")
    for i in range(4, 1, -1):
        print(salary[i])
    menu()

menu()
