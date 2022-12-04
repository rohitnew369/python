print('''Calcuator made by rohit😉 \n''')

num1 = int(input("\nEnter the first number \n --->"))
num2 = int(input("\nEnter the Second number \n --->"))

opration = input("\nEnter 1 to Add \nEnter 2 to Subtract \nEnter 3 to Multiply \nEnter 4 to Divide \n--->   ")

if opration == "1":
  print("\n Addition is --> ", int(num1) + int(num2))


if opration == "2":
  print("\n Subtraction is --> ", int(num1) - int(num2))


if opration == "3":
  print("\n Multiplication is --> ", int(num1) * int(num2))


if opration == "4":
  print("\n Division is --> ", int(num1) / int(num2))
