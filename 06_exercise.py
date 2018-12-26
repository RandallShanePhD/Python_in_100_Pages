# Python in 100 Pages - v2
# Loops Exercises

nums = [8, 6, 7, 5, 3, 0, 9]
evens = []
odds = []

for n in nums:
    if n % 2 == 0:
        evens.append(n)
    else:
        odds.append(n)

print('ORIGINAL LIST: ', nums)
print('EVENS: ', evens)
print('ODDS: ', odds)
