# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 19:31:14 2021

@author: nishant
"""
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from credential import email_id,password,chromedriver_path
from text_process import Node, process_data
from key import get_score
from bs4 import BeautifulSoup

def enter_meeting(browser,email_id,password,meeting_code):
    '''
    Input
    Browser Object
    Email ID
    Password
    Meeting Code 
    
    Description:
    This function helps to join the meeting in Google Meet
    
    '''
    browser.get('https://meet.google.com/')
    browser.find_element_by_xpath('/html/body/header/div[1]/div/div[3]/div[1]/div/span[1]/a').click()
    login_element = browser.find_element_by_xpath('//*[@id="identifierId"]')
    login_element.send_keys(email_id)
    browser.find_element_by_xpath('//*[@id="identifierNext"]/div/button/div[2]').click()
    time.sleep(10)
    password_element = browser.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
    password_element.send_keys(password)
    browser.find_element_by_xpath('//*[@id="passwordNext"]/div/button/div[2]').click()
    time.sleep(5)
    try :
        print("First Entering Method")
        browser.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[2]/div[2]/div/c-wiz/div[1]/div/div/div[1]/div').click()
        time.sleep(10)
        meeting_element = browser.find_element_by_xpath('//*[@id="yDmH0d"]/div[3]/div/div[2]/span/div/div[2]/div[1]/div[1]/input')
        meeting_element.send_keys(meeting_code)
        browser.find_element_by_xpath('//*[@id="yDmH0d"]/div[3]/div/div[2]/span/div/div[4]/div[2]/div/span/span').click()
    except:
        print('Another Entering Method')
        meeting_element = browser.find_element_by_xpath('//*[@id="i3"]')
        meeting_element.click()
        time.sleep(3)
        meeting_element.send_keys(meeting_code)
        browser.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div[2]/div/div[1]/div[3]/div[2]/div[2]/button/div[2]').click()
    time.sleep(10)
    browser.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[3]/div[1]/div/div/div').click()
    browser.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[3]/div[2]/div/div').click()
    browser.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/span/span').click()
    time.sleep(30)
    
    return browser

def count_meeting(browser):
    '''
    Input
    Browser object
    
    Output
    
    Count of People attending the meeting
    
    Description
    This function will helps to know the people in the meeting
    
    '''
    
    count_element = browser.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[8]/div[3]/div[3]/div/div[2]/div[2]/div[1]/div[1]/span/div/span[2]')
    
    return int(count_element.text.strip('()')) 




def chat_detect(browser):
    '''
    Input
    Browser Object
    
    Description:
    This function helps to detect chat messages more functionalities have to be added
        
    '''

    browser.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[8]/div[3]/div[6]/div[3]/div/div[2]/div[3]/span/span').click()
    time.sleep(5)
    chat_element = browser.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[8]/div[3]/div[3]/div/div[2]/div[2]/div[2]/span[2]/div/div[2]')
    prev_div = 0 

    node = Node()
    offenders_count = {}

    while(count_meeting(browser) > 1):
        node = process_data(browser, node, offenders_count)
        browser.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[8]/div[3]/div[3]/div/div[2]/div[2]/div[1]/div[2]').click()
    
    browser.quit()    
    return 
    
if __name__ == "__main__":
        
    chrome_options = Options()
    chrome_options.add_argument('use-fake-ui-for-media-stream')
    chrome_options.add_argument('use-fake-device-for-media-stream')
    chrome_options.add_argument('allow-file-access-from-files')
    
    browser = webdriver.Chrome(chromedriver_path,chrome_options=chrome_options)
    
    browser = enter_meeting(browser,email_id,password,'awa-pdxc-gha')
    chat_detect(browser)
