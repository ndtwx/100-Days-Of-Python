# https://selenium-python.readthedocs.io/
# https://www.selenium.dev/documentation/webdriver/elements/locators/
from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1")

# How to find and select specific HTML Elements on a website with selenium?

# By class
# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole").text
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction").text
# print(f"The price is {price_dollar}.{price_cents}")

# By name
driver.get("https://www.python.org/")
# search_bar = driver.find_element(By.NAME, value='q')
# print(search_bar.get_attribute("placeholder"))
# button = driver.find_element(By.ID, value="submit")
# print(button.size)

# By CSS selector
# documentation_link = driver.find_element(By.CSS_SELECTOR, value='.documentation-widget a')
# print(documentation_link.text)

# By XPath
# https://www.w3schools.com/xml/xpath_intro.asp
xpath = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(xpath.text)

# close the active browser
# driver.close()
# close the entire browser
driver.quit()
