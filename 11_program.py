# Lesson 11
# Writing Programs

import csv
import os
import sys


data = {}
fname = 'dossier.csv'


def create():
    # Collect data
    print('Create Entry:')
    name = input('Name: ')
    job = input('Job: ')
    email = input('Email: ').lower()  # harmonize case
    phone = input('Phone: ')

    # Add the dictionary
    data[email] = {'name': name,
                   'job': job,
                   'phone': phone}


def read():
    # Check for data
    if len(data) > 0:
        for record in data:  # loop through
            entry = data[record]  # load data into entry dictionary
            print('Name: %s' % entry['name'])
            print('Job: %s' % entry['job'])
            print('Email: %s' % record)
            print('Phone: %s' % entry['phone'])
            print('\n')
    else:
        print('There are no records!')


def update():
    # Establish the record to change
    email = input('Enter the email of the record to modify: ')
    print('Enter modified info.\n (return if no change)')

    # Queue the update
    new = {}
    new['email'] = email
    new['name'] = input('Name: ')
    new['job'] = input('Job: ')
    new['phone'] = input('Phone: ')

    # Change the data
    # delete(data[email])  # delete the old record using the delete function
    data[email] = new  # add the new record


def delete(email=''):
    # Get the emal ena delete it
    if email == '':
        email = input('Enter the email to delete: ').lower()
    del data[email]


def save(fname):
    # use the filename variable & write the data
    # w+ mode means overwrite
    with open(fname, 'w+') as csvfile:
        writer = csv.writer(csvfile)
        for record in data:
            entry = data[record]
            row = [record,
                   entry['name'],
                   entry['job'],
                   entry['phone']]
            writer.writerow(row)


def load(fname):
    # Load the file and populate the data dictionary
    # NEED os and csv library
    if os.path.isfile(fname):
        records = {}
        with open(fname, 'r') as csvfile:
            csv_data = csv.reader(csvfile, delimiter=',')
            for row in csv_data:
                records[row[0]] = {'name': row[1],
                                   'job': row[2],
                                   'phone': row[3]}
        data.update(records)
    return data


def search():
    # NOTE: this is very rudimentary search

    # Setup results list
    results = []

    # Collect the search term
    print('Enter field to search:')
    field = input('(E)mail, (N)ame, (J)ob, (P)hone: ').upper()
    term = input('Enter search term: ')

    # Look thru the fields and add to results
    if field.upper() == 'E':
        field = 'email'
        results = [x for x in data if x == term]
    else:
        if field.upper() == 'N':
            field = 'name'
        elif field.upper() == 'J':
            field = 'job'
        elif field.upper() == 'P':
            field = 'phone'
        results = [x for x in data if term in data[x][field]]

    # Display the search results
    if len(results) > 0:
        print('Search Results: ')
        for result in results:
            entry = data[result]
            print('\tName: %s' % entry['name'])
            print('\tJob: %s' % entry['job'])
            print('\tEmail: %s' % result)
            print('\tPhone: %s' % entry['phone'])
            print('\n')
    else:
        print('There are no Search Results!')


if __name__ == '__main__':
    print('Welcome to the Dossier!')
    data = load(fname)

    while True:  # while loop
        print('\tThere are %i records.' % len(data))
        print('\tMenu: (C)reate, (R)ead, (U)pdate, (D)elete, (S)earch, (Q)uit')
        action = input('\tEnter Action: ').upper()  # upper case
        action = action.upper()
        print('\n')

        # Interpret input
        try:
            if action == 'C':
                create()
            elif action == 'R':
                read()
            elif action == 'U':
                update()
            elif action == 'D':
                delete()
            elif action == 'S':
                search()
            elif action == 'Q':
                save(fname)
                sys.exit()
            else:
                print('Please pick a valid action!\n')
        except:
            print('\nSomething went wrong, try again!\n')
            pass
