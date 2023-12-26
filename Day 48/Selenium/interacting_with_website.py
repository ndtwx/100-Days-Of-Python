# https://selenium-python.readthedocs.io/
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

# driver.get("https://en.wikipedia.org/wiki/Main_Page")
"""
how to click the link in the website using selenium?
"""
# article_count = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/a[1]')
# article_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
# article_count.click()
# print(article_count.text)

# # Find element by Link Text
# all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# # all_portals.click()

"""
Sending keyboard input to search bar and press enter
"""
# # Find the "Search" <input> by Name
# search = driver.find_element(By.NAME, value="search")
#
# # Sending keyboard input to search bar and press enter
# search.send_keys("Python", Keys.ENTER)

"""
filling up forms
"""
driver.get("https://secure-retreat-92358.herokuapp.com/")

f_name = driver.find_element(By.NAME, value="fName")
f_name.send_keys("Andy")

l_name = driver.find_element(By.NAME, value="lName")
l_name.send_keys("Tang")

email = driver.find_element(By.NAME, value="email")
email.send_keys("nd_twx@hotmail.com")

sign_up = driver.find_element(By.CLASS_NAME, value="btn")
# Find using CSS SELECTOR
# sign_up = driver.find_element(By.CSS_SELECTOR, value="form button")
sign_up.click()
