import class_calculator as cc


def calculator(num1, num2):
    try:
        num1 = int(num1)
        num2 = int(num2)

        # Addition of 2 Classes
        cc1 = cc.ClassCalculator(num1)
        cc2 = cc.ClassCalculator(num2)
        addition = cc1 + cc2
        print("Sum of two classes is {}".format(addition))

        # Addition of Class and Number
        cc3 = cc.ClassCalculator(num1)
        addition = cc3 + num2
        print("Sum of Class and Number is {}".format(addition))

        # Subtraction of 2 Classes
        cc4 = cc.ClassCalculator(num1)
        cc5 = cc.ClassCalculator(num2)
        subtraction = cc4 - cc5
        print("Subtraction of two classes is {}".format(subtraction))

        # Subtraction of Class and Number
        cc6 = cc.ClassCalculator(num1)
        subtraction = cc6 - num2
        print("Subtraction of Class and Number is {}".format(subtraction))

        # Multiplication of 2 Classes
        cc7 = cc.ClassCalculator(num1)
        cc8 = cc.ClassCalculator(num2)
        multiplication = cc7 * cc8
        print("Multiplication of two classes is {}".format(multiplication))

        # Multiplication of Class and Number
        cc9 = cc.ClassCalculator(num1)
        multiplication = cc9 * num2
        print("Multiplication of Class and Number is {}".format(multiplication))

    except ValueError:
        print("Entered value should be in number format")


enter_num1 = input("Enter 1st Number: ")
enter_num2 = input("Enter 2nd Number: ")
calculator(enter_num1, enter_num2)
