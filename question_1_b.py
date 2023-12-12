"""
Ask users to input one number, the number will be the size of a square . Using the print
function to dr aw this square.
Need input size.
The output will be a single square created by the print function.
Examples:
When size = 1 => *
When size = 2 => * *
                 * *
When size = 3 => * * *
                 *   *
                 * * *
When size = 4 => => * * * *
                    *     *
                    *     *
                    * * * *   
Group Name: [Group 110 DAR]

Group Members:
[Name: Krishna Prasad Subedi] -[ID: S371919]
[Name: Saurav Ghimire] -[ID: S375203]
[Name: Rabi Acharya] -[ID: S372977]
[Name: Ranjit Kunwar] -[ID: S375204]
[Name: Muhammad Waqas Ashraf]- [ID: S374681]

"""

try:
    # Get user input for the size of the square
    size = int(input("Enter the size of the square: "))

    # Check if the size is non-negative
    if size > 0:
        # Print the hollow square pattern
        for i in range(size):
            for j in range(size):
                if i == 0 or i == size - 1 or j == 0 or j == size - 1:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()  # Move to the next line after printing each row
    else:
        print("Please enter a positive integer for the size of the square.")

except ValueError:
    print("Please enter a valid integer for the size of the square.")
