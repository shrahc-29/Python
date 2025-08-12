print("Python Program complex number calculator.\n")

#Python program to write a calculator for complex numbers.

import cmath

class ComplexCal:

    def TakeNums(self):  # Function to take input of the numbers
        self.num1 = complex(input("Enter first complex number: "))
        self.num2 = complex(input("Enter second complex number: "))
        print("\n")

    def add(self):  # Method to add the numbers
        add = self.num1 + self.num2
        print("Addition of the two complex numbers is: ", add)
        print("\n")

    def sub(self):  # Method to subtract the numbers
        sub = self.num1 - self.num2
        print("Difference of the two complex numbers is: ", sub)
        print("\n")

    def prod(self):  # Method to multiply the numbers
        prod = self.num1 * self.num2
        print("Product of the two complex numbers is: ", prod)
        print("\n")

    def div(self):  # Method to divide the numbers
        if self.num2 == 0:
            print("Division by zero is not possible. ")
            print("\n")
        else:
            div = self.num1 / self.num2
            print("Division of the two complex numbers is: ", div)
            print("\n")


# Creating an object of the class 'ComplexCal'
calc = ComplexCal()

# Taking input of the numbers
calc.TakeNums()

# Entering choice of operator
print(" 1) Addition\n 2) Subtraction\n 3) Multiplication\n 4) Division\n 5) Exit Calculator\n")
choice = input("Enter your operator choice as given above: ")
print("\n")

while choice != '5':
    if choice == '1':
        calc.add()
    elif choice == '2':
        calc.sub()
    elif choice == '3':
        calc.prod()
    elif choice == '4':
        calc.div()
    elif choice == '5':
        print("Exiting the calculator.")
        break
    else:
        print("Invalid choice")

    # Ask for the next choice
    print("\n 1) Addition\n 2) Subtraction\n 3) Multiplication\n 4) Division\n 5) Exit Calculator\n")
    choice = input("Enter your operator choice as given above: ")
    print("\n")
