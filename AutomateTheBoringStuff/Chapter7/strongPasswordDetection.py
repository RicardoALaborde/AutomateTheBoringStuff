'''
Write a function that uses regular expressions to make sure the password string it is passed is strong. A strong password is defined as one that is at least eight characters long, contains both uppercase and lowercase characters, and has at least one digit. You may need to test the string against multiple regex patterns to validate its strength.
'''

import re

def isStrong(password):
    hasUpper = re.compile(r'[A-Z]')
    hasLower = re.compile(r'[a-z]')
    hasDigit = re.compile(r'[0-9]')
    if len(password) >= 8:
        if hasUpper.search(password) != None:
            if hasLower.search(password) != None:
                if hasDigit.search(password) != None:
                    return True
                else:
                    print('This password is not strong. Password must have a digit.')
            else:
                print('This password is not strong. Password must have at least one lowercase character.')
        else:
            print('This password is not strong. Password must have at least one uppercase character.')
    else:
        print('This password is not strong. Password must be at least 8 characters long.')

myPassword = input('Enter your new password:')

if isStrong(myPassword):
    print('This password is super strong!')

