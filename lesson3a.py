# Boolean - This is a data type that evaluates either to true or false

isRaining = False
print(isRaining)
print(type(isRaining))

paidLoan = True
print(paidLoan)
print(type(paidLoan))

# comparison operators: They are used to compare between two statements and usually return a boolean answerr.

number1 = 2
number2 = 5

print("is number1 greater than number2?", number1 > number2)
print("is number1 greater than number2?", number1 < number2)
print("is number1 greater than number2?", number1 >= number2)
print("is number1 greater than number2?", number1 <= number2)
print("is number1 greater than number2?", number1 == number2)
print("is number1 greater than number2?", number1 != number2)

# logical operators
# logical AND-it returns if and only if the statements evaluates to true
print((3>1) and (7>6))

# logical OR-it evaluates to true if one of the conditions is true
print((3>1) or (7>6))

# logical NOT -it is used to negate a statement or condition
print(not(90>70))