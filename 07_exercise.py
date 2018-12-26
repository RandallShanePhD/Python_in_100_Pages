# Python in 100 Pages - v2
# Math Exercise

numbers = [74, 29, 49, 93, 68, 5, 34]

# Add the set
total = sum(numbers)

# Multiply the total by the maximum value
answer = total * max(numbers)

# Subtract 9999
# NOTE: we are overwriting the value of the answer variable
answer = answer - 99999

# divide by the minimum
answer = answer / min(numbers)

# print the answer
print('The answer is: ', answer)
