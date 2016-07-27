'''
Title: 2048 

2048 is a simple game where you combine tiles by sliding them up, down, left, or right with the arrow keys. 
You can actually get a fairly high score by repeatedly sliding in an up, right, down, and left pattern over and over again. 
Write a program that will open the game at https://gabrielecirulli.github.io/2048/ and keep sending up, right, down, and 
left keystrokes to automatically play the game.

Author: Ricardo Laborde
'''

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Firefox()
actionsTab=ActionChains(browser)
browser.get('https://gabrielecirulli.github.io/2048/')
actionsTab.send_keys(Keys.TAB)
actionsTab.send_keys(Keys.TAB)
actionsTab.perform()
while True:
    try:
        tryAgain = browser.find_element_by_link_text('Try again')
        break
    except:
        actions=ActionChains(browser)
        actions.send_keys(Keys.DOWN,Keys.RIGHT,Keys.UP,Keys.LEFT)
        time.sleep(1)
        actions.perform()

