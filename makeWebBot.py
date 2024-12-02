# This script will help you to automate Websites with Python. You can build a web bot that can control any website. Check out the below code. This script is handy in web scraping and web automation.
# pip install selenium

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

bot = webdriver.Chrome("chromedriver.exe")
bot.get('[http://www.google.com'](http://www.google.com'))

search = bot.find_element_by_name('q')
search.send_keys("@codedev101")
search.send_keys(Keys.RETURN)
time.sleep(5)
bot.quit()
