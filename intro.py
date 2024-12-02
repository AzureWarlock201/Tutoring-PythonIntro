print ("Welcome to calculator")
print ("Please choose 1 of the following operations")
print ("1. Add")
print ("2. Subtract")
print ("3. Multiply")
print ("4. Divide")
print ("5. Divide with remainder")
print ("6. Exponents")
operation = int(input (""))
numberOne = float(input ("Please type in your first number "))
numberTwo = float(input ("Please type in your second number "))
if operation == 1:
    print (numberOne, "+", numberTwo, "=", numberOne+numberTwo)
elif operation == 2:
    print (numberOne, "-", numberTwo, "=", numberOne-numberTwo)
elif operation == 3:
    print (numberOne, "x", numberTwo, "=", numberOne*numberTwo)
elif operation == 4:
    print (numberOne, "/", numberTwo, "=", numberOne/numberTwo)
elif operation == 5:
     print (numberOne, "/", numberTwo, "=", int(numberOne/numberTwo), "R:", numberOne%numberTwo)
elif operation == 6:
    print (numberOne, "^", numberTwo, "=", numberOne**numberTwo)
else:
    print ("Sorry, I can't do that.")