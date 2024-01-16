input_string = list(input("Enter the string 'Python': "))

if len(input_string) >= 2:
    del input_string[:2]

resultant_string = ''.join(reversed(input_string))

print("Reversed String:", resultant_string)

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2

print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
