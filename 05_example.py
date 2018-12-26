# Python in 100 Pages - v2
# If Statements Example

# Set initial variables
x = 9
y = 7
answer = 0


# Define the operation
operation = 'multiply'


# Evaluation code
if operation == 'add':
    answer = x + y
elif operation == 'subtract':
    answer = x - y
elif operation == 'multiply':
    answer = x * y
elif operation == 'divide':
    answer = x / y
else:
    print('Wrong operation!')

print( answer )
