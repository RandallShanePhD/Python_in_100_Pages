# Python in 100 Pages - v2
# Lists Example


# Create blank lists
cats = []
dogs = []

# Append values to the list
cats.append('Burbank')
cats.append('Sable')
cats.append('Georgio')
cats.append('Fiona')
dogs.append('Sidney')
dogs.append('Kingston')
dogs.append('Maya')
dogs.append('Grommitt')
dogs.append('Lola')
dogs.append('Diego')


# Combine the lists
pets = cats + dogs

# Sort the list in place
pets.sort()

# Display the pets list and length
print('pets list: ', pets)
print('length: ', len(pets))

# Removals
pets.remove('Burbank')
pets.remove('Sable')
pets.remove('Georgio')
pets.remove('Sidney')
pets.remove('Kingston')
pets.remove('Maya')
pets.remove('Grommitt')
pets.remove('Fiona')
pets.remove('Lola')

# Display the pets list
print('pets list: ', pets)


