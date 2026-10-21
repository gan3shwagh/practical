def binary():
    lst = sorted([54, 98, 12, 36, 321, 654, 987])
    left = 0
    right = len(lst) - 1
    target = int(input("Enter search target:"))
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == target:
            print(f"Element found at index:{mid}")
            return mid
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    print("Element not found")
    return -1

def linear():
    list = [54, 98, 12, 36, 321, 654, 987]
    target = int(input("entre search target\t"))
    for i in range(len(list)):
        if list[i] == target:
            return i
    return -1

def menu():
    print("welcome to searching technique\nchoose searching technique")
    op = input("\n1.\tBinary Search\n2.\tLinear Search\n3.\tExit\nSELECT")
    if op == "1":
        print(binary())
    elif op == "2":
        print(linear())
    elif op == "3":
        print("Exit.")
        return 1
    else:
        print("Invalid.")
    menu()

menu()
