# Python in 100 Pages - v2
# Dictionaries Example


# Create blank dictionary
session = { }


# Populate data units
session['user'] = 'Dave'
session['referred'] = 'web search'
print(session)


# Add home page visit
session['visited'] = ['home']
print(session)


# Append list with about page
session['visited'].append('about')
print(session)


# Clear the session
print(session)
session.clear()
print(session)


