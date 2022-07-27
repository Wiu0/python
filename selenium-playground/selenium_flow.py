from ast import Assert
from pprint import pprint
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time 
from selenium.webdriver.chrome.options import Options

class SeleniumReader:

    def __init__(self,path_chromeddriver, url):
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-ssl-errors=yes')
        options.add_argument('--ignore-certificate-errors')
        self.driver = webdriver.Chrome(path_chromeddriver, options=options)
        self.driver.get(url)

    def findByTextBox(self, by, value, name):
        elem = self.driver.find_element(by, value)
        elem.clear()
        elem.send_keys(name)
        elem.send_keys(Keys.RETURN)
        time.sleep(2)
    
    def findByDiv(self, by, value):
        elem = self.driver.find_element(by, value)
        time.sleep(2)
        return elem
    
    def findByP(self, by, value):
        elem = self.driver.find_element(by, value)
        time.sleep(2)
        return elem

    def initCrawler(self, nameUser):
        self.findByTextBox(By.ID, "query", nameUser)
        list_dom_href = self.findByDiv(By.XPATH, "//*[@class='results members']")
        list_a_href = list_dom_href.find_elements(By.TAG_NAME, "a")
        time.sleep(2)
        for item in list_a_href:
            text = item.text
            print(text)
            item.send_keys(Keys.RETURN)
            break
            # .findElement(By.xpath("//a[@href='/docs/configuration']"))
        joined = self.findByP(By.CLASS_NAME, "joined").text
        print("Usuario", nameUser, "joined at: ", joined)
        # assert "Member since December 16, 2020" in joined
        self.driver.close()


#Teste
sel = SeleniumReader("/Users/wiu/chromedriver", "https://www.greenfoot.org/home")
sel.initCrawler("wiu")