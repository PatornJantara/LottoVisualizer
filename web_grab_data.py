from operator import truediv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as bs
import os
import requests
import wget
import zipfile
import shutil

class WebScrapper:

    def __init__(self):
        # Set up chromedriver    
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors') # ignore any error sending back
        options.add_argument('--incognito')     # Incognito mode (un-identify user)
        options.add_argument('--headless')      # Dont open up browser
        self.driver = webdriver.Chrome(os.getcwd() +"//chromedriver.exe", chrome_options=options)

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

    def check_driver_version(self):
        str1 = self.driver.capabilities['browserVersion']
        str2 = self.driver.capabilities['chrome']['chromedriverVersion'].split(' ')[0]
        print(str1)
        print(str2)
        print(str1[0:3])
        print(str2[0:3])
        if str1[0:3] != str2[0:3]: 
            self.update_driver()

    def update_driver(self):

        url = 'https://chromedriver.storage.googleapis.com/LATEST_RELEASE'
        response = requests.get(url)
        version_number = response.text
        download_url = "https://chromedriver.storage.googleapis.com/" + version_number +"/chromedriver_win32.zip"

        if  "chromedriver.zip" in os.listdir(os.getcwd()):
            os.remove(os.getcwd()+"//chromedriver.zip")

        # download the zip file using the url built above
        latest_driver_zip = wget.download(download_url,'chromedriver.zip')

        os.remove(os.getcwd()+"\\chromedriver.exe")

        # extract the zip file
        with zipfile.ZipFile(latest_driver_zip, 'r') as zip_ref:
            zip_ref.extractall() # you can specify the destination folder path here
        # delete the zip file downloaded above
        os.remove(latest_driver_zip)
            

    def Close(self):
         self.driver.close()
