# 10-7. Addition Calculator: Wrap your code from Exercise 10-6 in a while loop
# so the user can continue entering numbers even if they make a mistake and
# enter text instead of a number.

print("-\t-Addition Calculator-\t-")
print("Enter 'q' to exit\n")
while True:
    first_number = input("Enter the first number: ")
    if first_number=='q':
       print("Exiting...")
       break

    second_number = input("Enter the second number: ")
    if second_number=='q':
        print("Exiting...")
        break

    try:
        result = int(first_number) + int(second_number)
    except ValueError:
        print("You've entered a value that's not a number.\n")
    else:
        print(f"The sum of the given numbers is: {int(result)}\n")
