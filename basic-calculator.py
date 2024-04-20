#to make the script continue till end, needed to make a while loop and add a break statement
#Create menu for operations
while True:
    print("""Choose an operation:
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division
    5. Division with Remainder
    6. Exit
    """)
    # Take input from the user about which operation to perform
    total = int(input("Enter your choice: "))

    if total == 6:
        print("Exiting...")
        break  # Exit the loop when 6 is pressed

    a = float(input("Enter the first number: ")) # get first number
    b = float(input("Enter the second number: ")) # get second number

    # Perform the operation based on the user's choice

    if total == 1:
        print("Result:", a + b)
    elif total == 2:
        print("Result:", a - b)
    elif total == 3:
        print("Result:", a * b)
    elif total == 4:
        if b != 0:
            print("Result:", a / b)
        else:
            print("Cannot divide by zero!")
    elif total == 5:
        if b != 0:
            print("Result:", a % b)
        else:
            print("Cannot divide by zero!")
    else:
        print("Invalid Input. Try another number.")
