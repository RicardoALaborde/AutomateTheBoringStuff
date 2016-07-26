'''
Title: Command Line Emailer

Write a program that takes an email address and string of text
on the command line and then, using Selenium, logs into your
email account and sends an email of the string to the provided
address. (You might want to set up a separate email account for this program.)

This would be a nice way to add a notification feature to your programs.
You could also write a similar program to send messages from a Facebook or Twitter account.

Author: Ricardo Laborde
'''

from selenium import webdriver
import time
import sys

if len(sys.argv) < 4:
    exit()

email=sys.argv[1]
password=sys.argv[2]
toEmail=sys.argv[3]
subject=sys.argv[4]
body=sys.argv[5]

browser = webdriver.Firefox()
#Get into gmail
browser.get('https://accounts.google.com/ServiceLogin?service=mail&continue=https://mail.google.com/mail/#identifier')
try:
    loginElement = browser.find_element_by_id('Email')
    #enter your email here
    loginElement.send_keys("%s"%(email))
    loginElement.submit()
    #wait for gmail to submit login and showw password field
    time.sleep(3)
    passwordElement = browser.find_element_by_id('Passwd')
    #enter your password here
    passwordElement.send_keys('%s'%(password))
    passwordElement.submit()
    #wait for gmail to enter into your account
    time.sleep(10)
    composeElement = browser.find_element_by_css_selector('.T-I-KE')
    composeElement.click()
    #wait for compose message to come up
    time.sleep(4)
    toElement = browser.find_element_by_id(':os')
    #enter who youre going to send the email to
    toElement.send_keys('%s'%(toEmail))
    subjectElement = browser.find_element_by_id(':oc')
    #enter the subject of the email
    subjectElement.send_keys('%s'%(subject))
    bodyElement = browser.find_element_by_id(':ph')
    #enter the body of the message
    bodyElement.send_keys('%s'%(body))
    sendElement = browser.find_element_by_id(':o2')
    sendElement.click()
except:
    print('Error finding elements')
