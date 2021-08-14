from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as bs
import os

class WebScrapper:

    def __init__(self):
        # Set up chromedriver    
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors') # ignore any error sending back
        options.add_argument('--incognito')     # Incognito mode (un-identify user)
        options.add_argument('--headless')      # Dont open up browser
 
        self.driver = webdriver.Chrome(r'chromedriver.exe', chrome_options=options)

    def GetLotteryWeb(self,Web_url,targetHead,pageClass):

        self.driver.get(Web_url) 
        page = self.driver.page_source  
        soup = bs(page,'html.parser')  
        #head = soup.find_all('div',{'class':'block-title-page'}) 
        #content = soup.find_all('div',{'class':'block-st-all'})
        head = soup.find_all(targetHead,pageClass) 

        message = []

        for sub_head in head:
            message.append(sub_head.text.replace('\n',''))
      
        return message

    def Close(self):
         self.driver.close()

