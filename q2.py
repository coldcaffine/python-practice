# Q2) Problem statement: Develop a simple menu-driven Python program to create a
# list and perform the following operations: add an element using append(),
# remove an element using remove(), sort the list, and display the list. Use a
# loop to repeat the menu until the user selects Exit.

# Develop a simple menu-driven Python program to create a list and perform the following operations: add an element using append(), remove an element using remove(), sort the list, and display the list. Use a loop to repeat the menu until the user selects Exit.

numbers = [int(x)
           for x in input("Enter initial list (space separated): ").split()]

while True:
    print("\n---MENU---")
    print("1. Append")
    print("2. Remove")
    print("3. sort")
    print("4. Display")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        numbers.append(int(input("Enter element to append: ")))
    elif choice == "2":
        value = int(input("Enter element to remove: "))
        if value in numbers:
            numbers.remove(value)
        else:
            print("Element not found")
    elif choice == "3":
        numbers.sort()
        print("list sorted")
    elif choice == "4":
        print(numbers)
    elif choice == "5":
        print("Program terminates")
        break
    else:
        print("Invalid choice, try again")
