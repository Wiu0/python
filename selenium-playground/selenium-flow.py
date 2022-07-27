from ast import Assert
from pprint import pprint
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def findByTextBox(by, value):
    elem = driver.find_element(by, value)
    elem.clear()
    elem.send_keys("wiu")
    elem.send_keys(Keys.RETURN)
 
def findByDiv(by, value):
    elem = driver.find_element(by, value)
    return elem
 
def findByP(by, value):
    elem = driver.find_element(by, value)
    return elem

driver = webdriver.Chrome("/Users/wiu/chromedriver")
driver.get("https://www.greenfoot.org/home")
findByTextBox(By.ID, "query")
list_dom_href = findByDiv(By.XPATH, "//*[@class='results members']")
list_a_href = list_dom_href.find_elements(By.TAG_NAME, "a")
for item in list_a_href:
    text = item.text
    print(text)
    item.send_keys(Keys.RETURN)
    break
    # .findElement(By.xpath("//a[@href='/docs/configuration']"))
joined = findByP(By.CLASS_NAME, "joined").text
print(joined)
assert "Member since December 16, 2020" in joined
driver.close()
