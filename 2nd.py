class Calculator:

    def sq(self, num):
        return num ** 2

    def cube(self, num):
        return num ** 3

    def sqrt(self, num):
        return num ** 0.5


# Create ONE Calculator object
calc = Calculator()


def choice():
    while True:

        num = int(input("\nEnter a number: "))

        print("\n1. Square")
        print("2. Cube")
        print("3. Square Root")

        ch = int(input("Enter your choice: "))

        if ch == 1:
            print("Square =", calc.sq(num))

        elif ch == 2:
            print("Cube =", calc.cube(num))

        elif ch == 3:
            print("Square Root =", calc.sqrt(num))

        else:
            print("Invalid Choice")

        cont = input("\nDo you want to continue? (y/n): ")

        if cont.lower() == "n":
            print("Thank you for using the calculator!")
            break

choice()