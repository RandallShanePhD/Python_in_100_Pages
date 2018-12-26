# Python in 100 Pages - v2
# Loops Examples


# For Loop Example 1
# Initialize a list of numbers
numbers = [1, 2, 3, 4, 5]

# Set an answers variable
total = 0

# Operational loop
for num in numbers:
    print('Adding: ', num)
    total = total + num
    print('The total is: ', total)

# Final answer
print('Final Total: ', total)


# For Loop Example 2
numbers = [9, 4, 5, 1, 2, 8, 5, 7, 6, 3]
total = 0
up_to_20 = []            # defines an empty list
for num in numbers:      # continuous loop
    if total < 20:           # check the total and if it is less than 20…
        up_to_20.append(num) # append the list number to the up_to_20 list
        total += num         # increment total by the number
        print(up_to_20)      # print the list
    else:                    # so if the total is not less than 20…
        break                # then stop iterating


# For Loop Example 3
pops = {'NewYork': 11754213, 'Mexico City': 23634895, 'London': 9046485}

for city in pops:
    total += pops[city]



# While Loop Example
i = 0
threshold = 10
while i < threshold:
    print('I = ', i)
    i += 1
