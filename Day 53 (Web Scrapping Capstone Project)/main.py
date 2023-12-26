# https://forms.gle/QrBpemijNCunNbu6A
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

URL = "https://appbrewery.github.io/Zillow-Clone/"

response = requests.get(URL)
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")

# How to get hold of all the specify tag?
all_anchor_tags = soup.find_all(name="a", class_="StyledPropertyCardDataArea-anchor")

# Create a list of all the links on the page using a CSS Selector
all_link_elements = soup.select(".StyledPropertyCardDataWrapper a")
# Python list comprehension (covered in Day 26)
address_link_list = [link["href"] for link in all_link_elements]
print(f"There are {len(address_link_list)} links to individual listings in total: \n")
print(address_link_list)

# Create a list of all the addresses on the page using a CSS Selector
# Remove newlines \n, pipe symbols |, and whitespaces to clean up the address data
all_address_elements = soup.select(".StyledPropertyCardDataWrapper address")
address_list = [address.get_text().replace(" | ", " ").strip() for address in all_address_elements]
print(f"\n After having been cleaned up, the {len(address_list)} addresses now look like this: \n")
print(address_list)

# Create a list of all the prices on the page using a CSS Selector
# Get a clean dollar price and strip off any "+" symbols and "per month" /mo abbreviation
all_price_elements = soup.select(".PropertyCardWrapper span")
price_list = [price.get_text().replace("/mo", "").split("+")[0] for price in all_price_elements if "$" in price.text]
print(f"\n After having been cleaned up, the {len(price_list)} prices now look like this: \n")
print(price_list)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)


for n in range(len(address_link_list)):
    driver.get("https://forms.gle/QrBpemijNCunNbu6A")
    time.sleep(2)

    address_question = driver.find_element(By.XPATH,
                                           value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_question = driver.find_element(By.XPATH,
                                         value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_question = driver.find_element(By.XPATH,
                                        value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element(By.CSS_SELECTOR, value=".uArJ5e")

    address_question.send_keys(address_list[n])
    price_question.send_keys(price_list[n])
    link_question.send_keys(address_link_list[n])
    submit_button.click()

