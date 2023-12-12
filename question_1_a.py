"""Ask the user to input three numbers, and check if these three numbers can form a triangle
Need three inputs from user and the output shows whether the result can form a triangle or not.

Group Name: [Group 110 DAR]

Group Members:
[Name: Krishna Prasad Subedi] -[ID: S371919]
[Name: Saurav Ghimire] -[ID: S375203]
[Name: Rabi Acharya] -[ID: S372977]
[Name: Ranjit Kunwar] -[ID: S375204]
[Name: Muhammad Waqas Ashraf]- [ID: S374681]
"""
# Check whether triangle can be formed from inputs supplied


def check_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False


# Get user input
try:
    side1 = float(input("Enter the length of the first side: "))
    side2 = float(input("Enter the length of the second side: "))
    side3 = float(input("Enter the length of the third side: "))

    # Check if the sides can form a triangle
    if check_triangle(side1, side2, side3):
        print("These sides can form a triangle.")
    else:
        print("These sides cannot form a triangle.")

except ValueError:
    print("Please enter valid numerical values for the side lengths.")
