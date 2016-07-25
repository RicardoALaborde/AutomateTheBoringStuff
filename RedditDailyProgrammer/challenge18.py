'''
Often times in commercials, phone numbers contain letters so that they're easy to remember
(e.g. 1-800-VERIZON). Write a program that will convert a phone number that contains letters
into a phone number with only numbers and the appropriate dash. Click here to learn more
about the telephone keypad.

Example Execution: Input: 1-800-COMCAST Output: 1-800-266-2278
'''

import re

phoneKeys = {
'A':'2','B':'2','C':'2',
'D':'3','E':'3','F':'3',
'G':'4','H':'4','I':'4',
'J':'5','K':'5','L':'5',
'M':'6','N':'6','O':'6','P':'6',
'Q':'7','R':'7','S':'7',
'T':'8','U':'8','V':'8',
'W':'9','X':'9','Y':'9','Z':'9'
}

def convertToPhoneNumber(phone):
    phoneNumber = ''
    #regex for finding phone # in string
    phoneRegex = re.compile(r'''
        (\d)?
        (-?)
        (\d\d\d) #Area Code
        (-?)
        (\w{7}|\d{3}\w{4}|\w{3}\d{4}) #last 7 digits
    ''',re.VERBOSE)
    mo = phoneRegex.search(phone)
    if mo.group(1) != None:
        phoneNumber += mo.group(1)
    phoneNumber += mo.group(3)
    for i in mo.group(5):
         try:
             int(i)
             phoneNumber += i
         except:
            #check if value exists in dictionary
            if i in phoneKeys.keys():
                phoneNumber += phoneKeys[i]
    if len(phoneNumber) == 11:
        phoneNumber=phoneNumber[0]+'-'+phoneNumber[1:4]+'-'+phoneNumber[4:7]+'-'+phoneNumber[7:]
    elif len(phoneNumber) == 10:
        phoneNumber=phoneNumber[0:3]+'-'+phoneNumber[3:6]+'-'+phoneNumber[6:]
    print(phoneNumber)

convertToPhoneNumber(input('What is the phone number you want to convert? \n').upper())
