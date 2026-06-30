num1 = int(input("Enter number 1 : "))
num2 = int(input("Enter number 2 : "))
def calculator(a, b):
    sum = a + b
    print (f"Sum of 2 number is: {sum}\n")

    difference = a - b
    print (f"Difference of 2 number is: {difference}\n")

    product = a * b
    print (f"Product of 2 number is: {product}")

    quotient = a / b
    print (f"Quotient of 2 number is: {quotient}")

calculator(num1 , num2)
