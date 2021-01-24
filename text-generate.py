from selenium import webdriver
from getpass import getpass
import time
from selenium.webdriver.chrome.options import Options
import requests
from bs4 import BeautifulSoup

from credential import email_id,  password
from text_process import Node, process_data, prev_node_state

chrome_options = Options()
chrome_options.add_argument('use-fake-ui-for-media-stream')
chrome_options.add_argument('use-fake-device-for-media-stream')
chrome_options.add_argument('allow-file-access-from-files')

browser = webdriver.Chrome("C:/Users/kshit/workspace_python/Selenium WebDrivers/chromedriver.exe",chrome_options=chrome_options)
browser.get('https://meet.google.com/')
browser.find_element_by_xpath('/html/body/header/div[1]/div/div[3]/div[1]/div/span[1]/a').click()
login_element = browser.find_element_by_xpath('//*[@id="identifierId"]')
login_element.send_keys(email_id)
browser.find_element_by_xpath('//*[@id="identifierNext"]/div/button/div[2]').click()
time.sleep(5)
password_element = browser.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
password_element.send_keys(password)
browser.find_element_by_xpath('//*[@id="passwordNext"]/div/button/div[2]').click()
time.sleep(5)
   
browser.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[2]/div[2]/div/c-wiz/div[1]/div/div/div[1]/div').click()
time.sleep(5)
meeting_element = browser.find_element_by_xpath('//*[@id="yDmH0d"]/div[3]/div/div[2]/span/div/div[2]/div[1]/div[1]/input')
time.sleep(10)
meeting_element.send_keys('fwy-pyyz-pfd')
browser.find_element_by_xpath('//*[@id="yDmH0d"]/div[3]/div/div[2]/span/div/div[4]/div[2]/div/span/span').click()
time.sleep(20)
browser.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[3]/div[1]/div/div/div').click()
time.sleep(5)
browser.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[3]/div[2]/div/div').click()
time.sleep(5)
browser.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/span/span').click()
time.sleep(10)

browser.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[8]/div[3]/div[6]/div[3]/div/div[2]/div[3]/span/span').click()

node = Node()   # this stores the previous configuration of the iteration

for i in range(1000):
    soup = BeautifulSoup(browser.page_source, 'html.parser')

    mydivs = soup.findAll("div", {"class": "GDhqjd"})
    for k in range(node.prev, len(mydivs)):
        print(mydivs[k].find("div",{"class":"YTbUzc"}).get_text())

        arr = mydivs[k].find_all("div",{'class':'oIy2qc'})

        sr = (node.sents) if (k == node.prev) else 0 

        for ind in range(sr, len(arr)):
            print(arr[ind].get_text())

        print("*"*20)

    node.prev = len(mydivs) - 1
    if (len(mydivs) != 0):
        node.sents = len(mydivs[-1].find_all("div",{'class':'oIy2qc'})) - 1
    time.sleep(30)

browser.quit()