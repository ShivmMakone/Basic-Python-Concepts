num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

add = num1 + num2
sub = num1 - num2
mul = num1 * num2
div = num1 / num2 if num2 != 0 else "Undefined"

print("\nAddition:", add)
print("Subtraction:", sub)
print("Multiplication:", mul)
print("Division:", div)
